// Progressive enhancement only: every page reads fine with this file absent.
(function () {
  "use strict";

  var $ = function (sel, root) { return (root || document).querySelector(sel); };
  var $$ = function (sel, root) { return Array.prototype.slice.call((root || document).querySelectorAll(sel)); };

  function esc(s) {
    return String(s).replace(/[&<>"]/g, function (c) {
      return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c];
    });
  }

  // Notes use curly quotes; people type straight ones. Compare on neither.
  function norm(s) {
    return String(s).toLowerCase().replace(/[\u2018\u2019]/g, "'").replace(/[\u201c\u201d]/g, '"');
  }

  function typing(e) {
    var t = e.target;
    return t && (t.tagName === "INPUT" || t.tagName === "TEXTAREA" || t.tagName === "SELECT" || t.isContentEditable);
  }

  // "/" jumps to whichever search or filter box the page has.
  document.addEventListener("keydown", function (e) {
    if (e.key !== "/" || typing(e) || e.metaKey || e.ctrlKey) return;
    var box = $("[data-search]") || $("[data-filter-text]");
    if (box) { e.preventDefault(); box.focus(); }
  });

  // ---------------------------------------------------------------- note
  var note = $(".note");
  if (note) {
    var bar = $(".progress span");
    var body = $(".note-body");
    var links = $$(".toc a");  // the desktop rail only
    var targets = links.map(function (a) { return document.getElementById(a.getAttribute("href").slice(1)); });

    var tick = function () {
      var r = body.getBoundingClientRect();
      var total = r.height - window.innerHeight * 0.6;
      var p = Math.min(1, Math.max(0, -r.top / (total > 0 ? total : 1)));
      if (bar) bar.style.transform = "scaleX(" + p + ")";

      var active = 0;
      for (var i = 0; i < targets.length; i++) {
        if (targets[i] && targets[i].getBoundingClientRect().top < window.innerHeight * 0.3) active = i;
      }
      links.forEach(function (a, i) { a.classList.toggle("is-active", i === active); });
    };
    var queued = false;
    window.addEventListener("scroll", function () {
      if (queued) return;
      queued = true;
      requestAnimationFrame(function () { queued = false; tick(); });
    }, { passive: true });
    window.addEventListener("resize", tick);
    tick();

    // The phone menu closes itself once a section is picked.
    var menu = $(".toc-mobile");
    if (menu) menu.addEventListener("click", function (e) { if (e.target.closest("a")) menu.open = false; });

    // Left and right arrows walk the source chronologically.
    document.addEventListener("keydown", function (e) {
      if (typing(e) || e.metaKey || e.ctrlKey || e.altKey || e.shiftKey) return;
      var to = e.key === "ArrowLeft" ? note.dataset.prev : e.key === "ArrowRight" ? note.dataset.next : "";
      if (to) window.location.href = to;
    });
  }

  // ------------------------------------------------------ source listing
  var listing = $("[data-filterable]");
  if (listing) {
    var text = $("[data-filter-text]", listing);
    var thread = $("[data-filter-thread]", listing);
    var count = $("[data-filter-count]", listing);
    var empty = $("[data-filter-empty]", listing);
    var rows = $$(".row", listing);
    var groups = $$("[data-group]", listing);

    var params = new URLSearchParams(window.location.search);
    if (params.get("q")) text.value = params.get("q");
    if (params.get("thread")) thread.value = params.get("thread");

    var apply = function () {
      var words = norm(text.value).split(/\s+/).filter(Boolean);
      var t = thread.value;
      var shown = 0;
      rows.forEach(function (row) {
        var hay = norm(row.dataset.text);
        var ok = (!t || (" " + row.dataset.threads + " ").indexOf(" " + t + " ") >= 0) &&
          words.every(function (w) { return hay.indexOf(w) >= 0; });
        row.hidden = !ok;
        if (ok) shown++;
      });
      groups.forEach(function (g) {
        var n = $$(".row", g).filter(function (r) { return !r.hidden; }).length;
        g.hidden = !n;
        $("[data-group-count]", g).textContent = n;
      });
      var filtered = words.length || t;
      count.textContent = filtered ? shown + " of " + rows.length + " notes" : "";
      empty.hidden = shown > 0;

      var q = new URLSearchParams();
      if (text.value.trim()) q.set("q", text.value.trim());
      if (t) q.set("thread", t);
      var qs = q.toString();
      history.replaceState(null, "", window.location.pathname + (qs ? "?" + qs : ""));
    };
    text.addEventListener("input", apply);
    thread.addEventListener("change", apply);
    apply();
  }

  // ---------------------------------------------------------- home search
  var search = $("[data-search]");
  if (search) {
    var results = $("[data-search-results]");
    var scount = $("[data-search-count]");
    var index = null;
    var loading = null;

    var load = function () {
      if (!loading) {
        loading = fetch("/search.json").then(function (r) { return r.json(); }).then(function (d) {
          index = d.map(function (n) {
            n.hay = norm(n.t + " " + n.b + " " + n.q + " " + n.h + " " + n.s + " " + n.x);
            return n;
          });
          return index;
        });
      }
      return loading;
    };

    // One pass with every word at once, so a later word can never match
    // inside a <mark> tag an earlier word inserted.
    var mark = function (s, words) {
      var parts = words.filter(function (w) { return w.length > 1; })
        .map(function (w) { return w.replace(/[.*+?^${}()|[\]\\]/g, "\\$&"); });
      if (!parts.length) return esc(s);
      var re = new RegExp("(" + parts.join("|") + ")", "gi");
      return String(s).split(re).map(function (piece, i) {
        return i % 2 ? "<mark>" + esc(piece) + "</mark>" : esc(piece);
      }).join("");
    };

    var run = function () {
      var words = norm(search.value).split(/\s+/).filter(Boolean);
      if (!words.length) { results.hidden = true; results.innerHTML = ""; scount.textContent = ""; return; }
      load().then(function () {
        var hits = index.filter(function (n) { return words.every(function (w) { return n.hay.indexOf(w) >= 0; }); });
        // Title and question matches first; the rest keep newest-first order.
        hits.sort(function (a, b) {
          var sa = words.some(function (w) { return norm(a.t + a.q).indexOf(w) >= 0; }) ? 0 : 1;
          var sb = words.some(function (w) { return norm(b.t + b.q).indexOf(w) >= 0; }) ? 0 : 1;
          return sa - sb;
        });
        results.innerHTML = hits.slice(0, 30).map(function (n) {
          return '<li class="row"><a href="' + n.u + '">' +
            '<span class="row-date">' + esc(n.s) + " &middot; " + esc(n.d) + "</span>" +
            '<span class="row-body"><span class="row-title">' + mark(n.t, words) + "</span>" +
            '<span class="row-by">' + mark(n.b, words) + "</span>" +
            '<span class="row-q">' + mark(n.q, words) + "</span></span></a></li>";
        }).join("");
        results.hidden = !hits.length;
        scount.textContent = hits.length
          ? (hits.length > 30 ? "Showing 30 of " + hits.length + " notes" : hits.length + (hits.length === 1 ? " note" : " notes"))
          : "No notes match. Try one word, or browse by thread below.";
      });
    };
    search.addEventListener("focus", load, { once: true });
    search.addEventListener("input", run);
    search.addEventListener("keydown", function (e) {
      if (e.key === "Escape") { search.value = ""; run(); search.blur(); }
    });
  }
})();

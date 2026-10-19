// Kyne Robotics site behaviour: header state, mobile menu, reveal on scroll,
// videos that play only while visible, hero pause control and the contact form.
(function () {
  "use strict";

  var doc = document.documentElement;
  doc.classList.add("js");
  var reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  // Header: light glass bar once the dark hero has scrolled away.
  var header = document.querySelector(".site-header");
  var hero = document.querySelector(".hero");
  function updateHeader() {
    if (!header) return;
    var limit = hero ? hero.offsetHeight - 90 : 24;
    header.classList.toggle("is-solid", window.scrollY > limit);
  }
  updateHeader();
  window.addEventListener("scroll", updateHeader, { passive: true });
  window.addEventListener("resize", updateHeader);

  // Mobile menu
  var menu = document.getElementById("mobile-menu");
  var openBtn = document.querySelector("[data-menu-open]");
  var closeBtn = document.querySelector("[data-menu-close]");
  function setMenu(open) {
    if (!menu) return;
    menu.classList.toggle("is-open", open);
    menu.setAttribute("aria-hidden", open ? "false" : "true");
    if (openBtn) openBtn.setAttribute("aria-expanded", open ? "true" : "false");
    document.body.style.overflow = open ? "hidden" : "";
    if (open && closeBtn) closeBtn.focus();
    if (!open && openBtn) openBtn.focus();
  }
  if (openBtn) openBtn.addEventListener("click", function () { setMenu(true); });
  if (closeBtn) closeBtn.addEventListener("click", function () { setMenu(false); });
  document.addEventListener("keydown", function (e) {
    if (e.key === "Escape" && menu && menu.classList.contains("is-open")) setMenu(false);
  });
  if (menu) {
    menu.querySelectorAll("a").forEach(function (a) {
      a.addEventListener("click", function () { setMenu(false); });
    });
  }

  // Reveal on scroll
  var revealEls = document.querySelectorAll("[data-reveal]");
  if (!("IntersectionObserver" in window) || reduceMotion) {
    revealEls.forEach(function (el) { el.classList.add("is-in"); });
  } else {
    var revealer = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add("is-in");
          revealer.unobserve(entry.target);
        }
      });
    }, { rootMargin: "0px 0px -8% 0px", threshold: 0.08 });
    revealEls.forEach(function (el) { revealer.observe(el); });
  }

  // Videos marked data-autoplay play muted while on screen and pause off screen.
  // With reduced motion they stay on their poster until the visitor presses play.
  var autoVideos = document.querySelectorAll("video[data-autoplay]");
  function tryPlay(v) {
    if (v.dataset.userPaused === "1") return;
    var p = v.play();
    if (p && p.catch) p.catch(function () {});
  }
  autoVideos.forEach(function (v) {
    v.muted = true;
    // The pause event fires after pause() returns, so the observer's flag is cleared here.
    v.addEventListener("pause", function () {
      if (v.dataset.observerPause === "1") v.dataset.observerPause = "0";
      else v.dataset.userPaused = "1";
    });
    v.addEventListener("play", function () { v.dataset.userPaused = "0"; });
  });
  if (!reduceMotion && "IntersectionObserver" in window) {
    var player = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        var v = entry.target;
        if (entry.isIntersecting) {
          if (v.preload === "none") v.preload = "auto";
          tryPlay(v);
        } else if (!v.paused) {
          v.dataset.observerPause = "1";
          v.pause();
        }
      });
    }, { threshold: 0.25 });
    autoVideos.forEach(function (v) { player.observe(v); });
  }

  // Hero pause and play control
  var heroVideo = document.querySelector(".hero__media video");
  var heroToggle = document.querySelector(".hero__toggle");
  if (heroVideo && heroToggle) {
    var label = heroToggle.querySelector("[data-label]");
    function syncToggle() {
      var playing = !heroVideo.paused;
      heroToggle.setAttribute("aria-pressed", playing ? "false" : "true");
      if (label) label.textContent = playing ? "Pause video" : "Play video";
    }
    heroToggle.addEventListener("click", function () {
      if (heroVideo.paused) { heroVideo.dataset.userPaused = "0"; tryPlay(heroVideo); }
      else { heroVideo.pause(); }
    });
    heroVideo.addEventListener("play", syncToggle);
    heroVideo.addEventListener("pause", syncToggle);
    syncToggle();
  }

  // Contact form: compose an email to the address in data-email.
  var form = document.querySelector("form[data-email]");
  if (form) {
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      if (!form.reportValidity()) return;
      var data = new FormData(form);
      var lines = [];
      var labels = {
        name: "Name", email: "Email", company: "Company", role: "Role",
        interest: "Interested in", robot: "Robot status", site: "Site and industry", message: "Message"
      };
      Object.keys(labels).forEach(function (key) {
        var value = (data.get(key) || "").toString().trim();
        if (value) lines.push(labels[key] + ": " + value);
      });
      var subject = "Enquiry from " + (data.get("company") || data.get("name") || "the website");
      var href = "mailto:" + form.dataset.email +
        "?subject=" + encodeURIComponent(subject) +
        "&body=" + encodeURIComponent(lines.join("\n\n"));
      window.location.href = href;
      var status = form.querySelector(".form__status");
      if (status) {
        status.textContent = "Your email app should open with the message filled in. If it does not, write to " +
          form.dataset.email + " and we will pick it up from there.";
        status.classList.add("is-visible");
      }
    });
  }
})();

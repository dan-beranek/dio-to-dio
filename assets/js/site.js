(() => {
  const desktopMenus = [...document.querySelectorAll(".resource-nav")];

  const setDesktopMenuOpen = (menu, open) => {
    const trigger = menu.querySelector(".resource-trigger");
    menu.dataset.open = String(open);
    if (trigger) trigger.setAttribute("aria-expanded", String(open));
  };

  desktopMenus.forEach((menu) => {
    const trigger = menu.querySelector(".resource-trigger");
    if (!trigger) return;

    menu.addEventListener("pointerenter", (event) => {
      if (event.pointerType === "mouse") setDesktopMenuOpen(menu, true);
    });

    menu.addEventListener("pointerleave", (event) => {
      if (event.pointerType === "mouse" && !menu.contains(document.activeElement)) {
        setDesktopMenuOpen(menu, false);
      }
    });

    menu.addEventListener("focusin", () => setDesktopMenuOpen(menu, true));

    menu.addEventListener("focusout", (event) => {
      if (!menu.contains(event.relatedTarget) && !menu.matches(":hover")) {
        setDesktopMenuOpen(menu, false);
      }
    });

    trigger.addEventListener("click", () => setDesktopMenuOpen(menu, true));

    menu.addEventListener("keydown", (event) => {
      if (event.key === "Escape") {
        setDesktopMenuOpen(menu, false);
        trigger.blur();
      }
    });
  });

  document.addEventListener("click", (event) => {
    const link = event.target.closest(".mobile-menu-panel a");
    if (link) {
      const menu = link.closest(".mobile-menu");
      if (menu) menu.open = false;
    }
  });

  document.addEventListener("pointerdown", (event) => {
    desktopMenus.forEach((menu) => {
      if (!menu.contains(event.target)) setDesktopMenuOpen(menu, false);
    });

    document.querySelectorAll(".mobile-resource-nav[open]").forEach((menu) => {
      if (!menu.contains(event.target)) menu.open = false;
    });

    document.querySelectorAll(".mobile-menu[open]").forEach((menu) => {
      if (!menu.contains(event.target)) menu.open = false;
    });
  });

  document.addEventListener("keydown", (event) => {
    if (event.key !== "Escape") return;

    desktopMenus.forEach((menu) => {
      setDesktopMenuOpen(menu, false);
      const trigger = menu.querySelector(".resource-trigger");
      if (menu.contains(document.activeElement) && trigger) trigger.blur();
    });

    document.querySelectorAll("details[open]").forEach((menu) => {
      if (menu.matches(".mobile-resource-nav, .mobile-menu")) menu.open = false;
    });
  });
  const reportToc = document.querySelector("[data-report-toc]");
  if (reportToc) {
    const toggle = reportToc.querySelector(".report-toc-toggle");
    const panel = reportToc.querySelector(".report-toc-panel");
    const close = reportToc.querySelector(".report-toc-close");

    const setReportTocOpen = (open) => {
      reportToc.dataset.open = String(open);
      toggle.setAttribute("aria-expanded", String(open));
      panel.setAttribute("aria-hidden", String(!open));
    };

    toggle.addEventListener("click", () => {
      setReportTocOpen(reportToc.dataset.open !== "true");
    });

    close.addEventListener("click", () => {
      setReportTocOpen(false);
      toggle.focus();
    });

    panel.addEventListener("click", (event) => {
      if (event.target.closest("a")) setReportTocOpen(false);
    });

    document.addEventListener("pointerdown", (event) => {
      if (reportToc.dataset.open === "true" && !reportToc.contains(event.target)) {
        setReportTocOpen(false);
      }
    });

    document.addEventListener("keydown", (event) => {
      if (event.key === "Escape" && reportToc.dataset.open === "true") {
        setReportTocOpen(false);
        toggle.focus();
      }
    });
  }

})();

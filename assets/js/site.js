(() => {
  document.addEventListener("click", (event) => {
    const link = event.target.closest(".mobile-menu-panel a");
    if (link) {
      const menu = link.closest(".mobile-menu");
      if (menu) menu.open = false;
    }
  });

  document.addEventListener("pointerdown", (event) => {
    document.querySelectorAll(".resource-nav[open], .mobile-resource-nav[open]").forEach((menu) => {
      if (!menu.contains(event.target)) menu.open = false;
    });
    document.querySelectorAll(".mobile-menu[open]").forEach((menu) => {
      if (!menu.contains(event.target)) menu.open = false;
    });
  });

  document.addEventListener("keydown", (event) => {
    if (event.key !== "Escape") return;
    document.querySelectorAll("details[open]").forEach((menu) => {
      if (menu.matches(".resource-nav, .mobile-resource-nav, .mobile-menu")) menu.open = false;
    });
  });
})();

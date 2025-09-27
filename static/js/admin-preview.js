(function () {
  if (!document.body.classList.contains("preview-mode")) {
    return;
  }

  var targets = document.querySelectorAll('[data-admin-url]');
  targets.forEach(function (el) {
    el.addEventListener('click', function (evt) {
      if (el.dataset.adminUrl) {
        evt.preventDefault();
        window.top.location.href = el.dataset.adminUrl;
      }
    });
  });
})();

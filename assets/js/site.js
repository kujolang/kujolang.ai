(function () {
  'use strict';

  function copyText(text) {
    if (navigator.clipboard && window.isSecureContext) {
      return navigator.clipboard.writeText(text);
    }

    return new Promise(function (resolve, reject) {
      var helper = document.createElement('textarea');
      helper.value = text;
      helper.setAttribute('readonly', '');
      helper.style.position = 'fixed';
      helper.style.opacity = '0';
      document.body.appendChild(helper);
      helper.select();
      try {
        document.execCommand('copy');
        resolve();
      } catch (error) {
        reject(error);
      } finally {
        helper.remove();
      }
    });
  }

  function setCopiedState(button, status) {
    button.dataset.copied = 'true';
    button.setAttribute('aria-label', 'Install command copied');
    if (status) status.textContent = 'Copied to clipboard.';
    window.setTimeout(function () {
      button.dataset.copied = 'false';
      button.setAttribute('aria-label', 'Copy install command');
      if (status) status.textContent = '';
    }, 1800);
  }

  function enhanceCopyButtons() {
    document.querySelectorAll('[data-copy-code]').forEach(function (button) {
      button.addEventListener('click', function () {
        var block = button.closest('.sk-code-block');
        var text = block && block.querySelector('code');
        var status = button.closest('.tool-install-panel') && button.closest('.tool-install-panel').querySelector('[data-copy-status]');
        if (!text) return;
        copyText(text.textContent.trim()).then(function () {
          setCopiedState(button, status);
        });
      });
    });

    document.querySelectorAll('[data-copy-install]').forEach(function (button) {
      button.addEventListener('click', function () {
        var dialog = button.closest('[role="dialog"]');
        var field = dialog && dialog.querySelector('input');
        var status = dialog && dialog.querySelector('[data-copy-status]');
        if (!field) return;
        copyText(field.value).then(function () {
          setCopiedState(button, status);
        });
      });
    });
  }

  function enhanceDrawerLinks() {
    document.querySelectorAll('[data-sk-drawer] a').forEach(function (link) {
      link.addEventListener('click', function () {
        var drawer = link.closest('[data-sk-drawer]');
        var scrim = document.querySelector('[data-sk-drawer-scrim]');
        if (drawer) {
          drawer.hidden = true;
          drawer.setAttribute('aria-hidden', 'true');
        }
        if (scrim) scrim.hidden = true;
      });
    });
  }

  function enhanceQuickInstall() {
    var modal = document.querySelector('[data-quick-install-modal]');
    if (!modal) return;
    var dialog = modal.querySelector('[role="dialog"]');
    var previousFocus = null;

    function closeDrawer() {
      var drawer = document.querySelector('[data-sk-drawer]');
      var scrim = document.querySelector('[data-sk-drawer-scrim]');
      if (drawer) {
        drawer.hidden = true;
        drawer.setAttribute('aria-hidden', 'true');
      }
      if (scrim) scrim.hidden = true;
    }

    function openModal(trigger) {
      previousFocus = trigger || document.activeElement;
      closeDrawer();
      modal.hidden = false;
      document.body.classList.add('modal-open');
      window.requestAnimationFrame(function () { dialog.focus(); });
    }

    function closeModal() {
      modal.hidden = true;
      document.body.classList.remove('modal-open');
      if (previousFocus && typeof previousFocus.focus === 'function') previousFocus.focus();
    }

    document.querySelectorAll('[data-quick-install-open]').forEach(function (button) {
      button.addEventListener('click', function () { openModal(button); });
    });

    modal.querySelectorAll('[data-quick-install-close]').forEach(function (button) {
      button.addEventListener('click', closeModal);
    });

    modal.addEventListener('keydown', function (event) {
      if (event.key === 'Escape') {
        event.preventDefault();
        closeModal();
        return;
      }
      if (event.key !== 'Tab') return;
      var focusable = Array.prototype.slice.call(dialog.querySelectorAll('button, input, a[href], [tabindex]:not([tabindex="-1"])'));
      if (!focusable.length) return;
      var first = focusable[0];
      var last = focusable[focusable.length - 1];
      if (event.shiftKey && document.activeElement === first) {
        event.preventDefault();
        last.focus();
      } else if (!event.shiftKey && document.activeElement === last) {
        event.preventDefault();
        first.focus();
      }
    });
  }

  function init() {
    enhanceCopyButtons();
    enhanceDrawerLinks();
    enhanceQuickInstall();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();

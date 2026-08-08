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

  function enhanceMonoScramble() {
    if (!window.ScrambleDecode || window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;

    var selector = '[data-scramble-text]';
    var pool = '█▓▒░<>/\\#[]{}=+*01';
    var observer = null;

    function usesMonoFont(element) {
      return window.getComputedStyle(element).fontFamily.toLowerCase().indexOf('departure mono') !== -1;
    }

    function runScramble(element) {
      if (element.dataset.scrambleComplete === 'true') return;
      var original = element.dataset.scrambleText || element.textContent;
      if (!original.trim()) return;

      element.dataset.scrambleComplete = 'true';
      element.setAttribute('aria-label', original);
      window.ScrambleDecode.scramble(element, {
        text: original,
        duration: 680 + Math.min(420, original.length * 12),
        pool: pool
      }).finished.then(function () {
        element.textContent = original;
      });
    }

    function observeScramble(element) {
      if (observer) observer.observe(element);
      else runScramble(element);
    }

    function wrapTextNode(node) {
      var parent = node.parentElement;
      if (!parent || !node.nodeValue.trim() || parent.closest(selector)) return;
      if (/^(SCRIPT|STYLE|NOSCRIPT|TEMPLATE|SVG)$/i.test(parent.tagName) || !usesMonoFont(parent)) return;

      var match = node.nodeValue.match(/^(\s*)([\s\S]*?)(\s*)$/);
      var original = match && match[2];
      if (!original) return;

      var fragment = document.createDocumentFragment();
      if (match[1]) fragment.appendChild(document.createTextNode(match[1]));
      var span = document.createElement('span');
      span.dataset.scrambleText = original;
      span.textContent = original;
      fragment.appendChild(span);
      if (match[3]) fragment.appendChild(document.createTextNode(match[3]));
      node.parentNode.replaceChild(fragment, node);
      observeScramble(span);
    }

    function findMonoText(root) {
      if (root.nodeType === Node.TEXT_NODE) {
        wrapTextNode(root);
        return;
      }
      if (root.nodeType !== Node.ELEMENT_NODE || root.closest(selector)) return;

      var walker = document.createTreeWalker(root, NodeFilter.SHOW_TEXT);
      var nodes = [];
      while (walker.nextNode()) nodes.push(walker.currentNode);
      nodes.forEach(wrapTextNode);
    }

    if ('IntersectionObserver' in window) {
      observer = new IntersectionObserver(function (entries) {
        entries.forEach(function (entry) {
          if (!entry.isIntersecting) return;
          observer.unobserve(entry.target);
          runScramble(entry.target);
        });
      }, { rootMargin: '0px 0px -12% 0px', threshold: 0.25 });
    }

    findMonoText(document.body);

    var mutationObserver = new MutationObserver(function (mutations) {
      mutations.forEach(function (mutation) {
        mutation.addedNodes.forEach(function (node) {
          if (node.parentElement && node.parentElement.closest(selector)) return;
          findMonoText(node);
        });
      });
    });
    mutationObserver.observe(document.body, { childList: true, subtree: true });
  }

  function init() {
    enhanceCopyButtons();
    enhanceDrawerLinks();
    enhanceQuickInstall();
    enhanceMonoScramble();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();

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

  function enhanceHomeDither() {
    var canvas = document.querySelector('[data-home-dither]');
    if (!canvas) return;

    var media = canvas.closest('.home-hero__media');
    var image = media && media.querySelector('img');
    var context = canvas.getContext('2d', { willReadFrequently: true });
    var sourceCanvas = document.createElement('canvas');
    var sourceContext = sourceCanvas.getContext('2d', { willReadFrequently: true });
    var sourcePixels = null;
    var frame = 0;
    var lastTick = 0;
    var resizeFrame = 0;
    var reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    var bayer8 = [
      [0, 48, 12, 60, 3, 51, 15, 63],
      [32, 16, 44, 28, 35, 19, 47, 31],
      [8, 56, 4, 52, 11, 59, 7, 55],
      [40, 24, 36, 20, 43, 27, 39, 23],
      [2, 50, 14, 62, 1, 49, 13, 61],
      [34, 18, 46, 30, 33, 17, 45, 29],
      [10, 58, 6, 54, 9, 57, 5, 53],
      [42, 26, 38, 22, 41, 25, 37, 21]
    ];

    if (!media || !image || !context || !sourceContext) return;

    function sizeCanvas() {
      var width = Math.max(1, Math.ceil(media.clientWidth / 2));
      var height = Math.max(1, Math.ceil(media.clientHeight / 2));
      canvas.width = width;
      canvas.height = height;
      sourceCanvas.width = width;
      sourceCanvas.height = height;

      var scale = Math.max(width / image.naturalWidth, height / image.naturalHeight);
      var drawWidth = image.naturalWidth * scale;
      var drawHeight = image.naturalHeight * scale;
      sourceContext.clearRect(0, 0, width, height);
      sourceContext.drawImage(image, width - drawWidth, (height - drawHeight) / 2, drawWidth, drawHeight);
      sourcePixels = sourceContext.getImageData(0, 0, width, height);
    }

    function drawFrame() {
      if (!sourcePixels) return;
      var width = canvas.width;
      var height = canvas.height;
      var output = context.createImageData(width, height);
      var source = sourcePixels.data;
      var target = output.data;
      var driftX = Math.floor(frame / 2) % 8;
      var driftY = Math.floor(frame / 3) % 8;
      var thresholdShift = reducedMotion ? 0 : Math.sin(frame * 0.36) * 7;

      for (var y = 0; y < height; y += 1) {
        for (var x = 0; x < width; x += 1) {
          var index = (y * width + x) * 4;
          var luminance = 0.299 * source[index] + 0.587 * source[index + 1] + 0.114 * source[index + 2];
          luminance = (luminance - 128) * 1.12 + 128;
          var matrix = bayer8[(y + driftY) % 8][(x + driftX) % 8];
          var threshold = 94 + matrix * 1.88 + thresholdShift;
          var value = luminance > threshold ? 244 : 14;
          target[index] = value;
          target[index + 1] = value;
          target[index + 2] = value;
          target[index + 3] = 255;
        }
      }

      context.putImageData(output, 0, 0);
      canvas.dataset.ditherReady = 'true';
      frame += 1;
    }

    function render(now) {
      if (now - lastTick >= 1000 / 14) {
        lastTick = now;
        drawFrame();
      }
      window.requestAnimationFrame(render);
    }

    function setup() {
      sizeCanvas();
      drawFrame();
      if (!reducedMotion) window.requestAnimationFrame(render);
    }

    function handleResize() {
      window.cancelAnimationFrame(resizeFrame);
      resizeFrame = window.requestAnimationFrame(function () {
        sizeCanvas();
        drawFrame();
      });
    }

    if (image.complete && image.naturalWidth) setup();
    else image.addEventListener('load', setup, { once: true });
    window.addEventListener('resize', handleResize);
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
    enhanceHomeDither();
    enhanceMonoScramble();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();

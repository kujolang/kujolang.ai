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
    var copyLabel = button.dataset.copyLabel || 'Copy install command';
    var copiedLabel = button.dataset.copiedLabel || 'Install command copied';
    button.dataset.copied = 'true';
    button.setAttribute('aria-label', copiedLabel);
    if (status) status.textContent = 'Copied to clipboard.';
    window.setTimeout(function () {
      button.dataset.copied = 'false';
      button.setAttribute('aria-label', copyLabel);
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

    document.querySelectorAll('[data-copy-agent-prompt]').forEach(function (button) {
      button.addEventListener('click', function () {
        var dialog = button.closest('[role="dialog"]');
        var field = dialog && dialog.querySelector('[data-agent-prompt-text]');
        var status = dialog && dialog.querySelector('[data-copy-status]');
        if (!field || !field.value.trim()) return;
        copyText(field.value).then(function () {
          setCopiedState(button, status);
        });
      });
    });
  }

  function enhanceMobileNavigation() {
    var toggle = document.querySelector('[data-mobile-menu-toggle]');
    var label = toggle && toggle.querySelector('[data-mobile-menu-label]');
    var shell = document.querySelector('[data-mobile-menu-shell]');
    var drawer = document.querySelector('[data-mobile-navigation]');
    var scrim = document.querySelector('[data-mobile-menu-scrim]');
    if (!toggle || !label || !shell || !drawer) return;

    function isOpen() {
      return !drawer.hidden;
    }

    function setOpen(open, restoreFocus) {
      drawer.hidden = !open;
      drawer.setAttribute('aria-hidden', String(!open));
      if (scrim) scrim.hidden = !open;
      shell.classList.toggle('is-open', open);
      document.body.classList.toggle('mobile-menu-open', open);
      toggle.setAttribute('aria-expanded', String(open));
      toggle.setAttribute('aria-label', open ? 'Close, close navigation' : 'Menu, open navigation');
      label.textContent = open ? 'Close' : 'Menu';
      if (open) {
        var firstLink = drawer.querySelector('a, button');
        if (firstLink) window.requestAnimationFrame(function () { firstLink.focus(); });
      } else if (restoreFocus) {
        toggle.focus();
      }
    }

    toggle.addEventListener('click', function () {
      setOpen(!isOpen(), false);
    });

    drawer.querySelectorAll('a, [data-quick-install-open]').forEach(function (control) {
      control.addEventListener('click', function () { setOpen(false, false); });
    });

    if (scrim) scrim.addEventListener('click', function () { setOpen(false, true); });

    document.addEventListener('kujo:close-mobile-menu', function () { setOpen(false, false); });
    document.addEventListener('keydown', function (event) {
      if (!isOpen()) return;
      if (event.key === 'Escape') {
        event.preventDefault();
        setOpen(false, true);
        return;
      }
      if (event.key !== 'Tab') return;
      var focusable = [toggle].concat(Array.prototype.slice.call(drawer.querySelectorAll('a[href], button:not([disabled]), [tabindex]:not([tabindex="-1"])')));
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

  function enhanceNavigationDropdowns() {
    document.querySelectorAll('[data-nav-dropdown]').forEach(function (dropdown) {
      var toggle = dropdown.querySelector('[data-nav-dropdown-toggle]');
      var menu = dropdown.querySelector('[data-nav-submenu]');
      if (!toggle || !menu) return;

      function setOpen(open) {
        menu.hidden = !open;
        toggle.setAttribute('aria-expanded', String(open));
        toggle.setAttribute('aria-label', (open ? 'Hide' : 'Show') + ' Ecosystem menu');
        dropdown.classList.toggle('is-open', open);
      }

      toggle.addEventListener('click', function () {
        setOpen(menu.hidden);
      });
      dropdown.addEventListener('keydown', function (event) {
        if (event.key === 'Escape' && !menu.hidden) {
          event.preventDefault();
          setOpen(false);
          toggle.focus();
        }
      });
      document.addEventListener('click', function (event) {
        if (!dropdown.contains(event.target)) setOpen(false);
      });
    });
  }

  function enhanceInstallModals() {
    var quickModal = document.querySelector('[data-quick-install-modal]');
    var agentModal = document.querySelector('[data-agent-prompt-modal]');
    if (!quickModal || !agentModal) return;
    var currentModal = null;
    var previousFocus = null;

    function closeDrawer() {
      document.dispatchEvent(new Event('kujo:close-mobile-menu'));
    }

    function openModal(modal, trigger) {
      if (!currentModal) previousFocus = trigger || document.activeElement;
      closeDrawer();
      if (currentModal) currentModal.hidden = true;
      modal.hidden = false;
      currentModal = modal;
      document.body.classList.add('modal-open');
      var dialog = modal.querySelector('[role="dialog"]');
      window.requestAnimationFrame(function () { dialog.focus(); });
    }

    function closeModal(modal) {
      modal.hidden = true;
      if (currentModal === modal) currentModal = null;
      document.body.classList.remove('modal-open');
      var restore = previousFocus;
      if (restore && restore.closest && restore.closest('[hidden]')) restore = document.querySelector('[data-mobile-menu-toggle]');
      if (restore && typeof restore.focus === 'function') restore.focus();
      previousFocus = null;
    }

    document.querySelectorAll('[data-quick-install-open]').forEach(function (button) {
      button.addEventListener('click', function () { openModal(quickModal, button); });
    });

    document.querySelectorAll('[data-agent-prompt-open]').forEach(function (link) {
      link.addEventListener('click', function (event) {
        event.preventDefault();
        var field = agentModal.querySelector('[data-agent-prompt-text]');
        openModal(agentModal, link);
        if (!field || field.dataset.loaded === 'true') return;
        fetch(link.href).then(function (response) {
          if (!response.ok) throw new Error('Prompt request failed');
          return response.text();
        }).then(function (text) {
          field.value = text.trim();
          field.dataset.loaded = 'true';
          var copyButton = agentModal.querySelector('[data-copy-agent-prompt]');
          if (copyButton) copyButton.disabled = false;
        }).catch(function () {
          field.value = 'The onboarding prompt could not be loaded. Open ' + link.href + ' to view and copy it.';
        });
      });
    });

    function bindModal(modal, closeSelector) {
      var dialog = modal.querySelector('[role="dialog"]');
      modal.querySelectorAll(closeSelector).forEach(function (button) {
        button.addEventListener('click', function () { closeModal(modal); });
      });
      modal.addEventListener('keydown', function (event) {
        if (event.key === 'Escape') {
          event.preventDefault();
          closeModal(modal);
          return;
        }
        if (event.key !== 'Tab') return;
        var focusable = Array.prototype.slice.call(dialog.querySelectorAll('button, input, textarea, a[href], [tabindex]:not([tabindex="-1"])'));
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

    bindModal(quickModal, '[data-quick-install-close]');
    bindModal(agentModal, '[data-agent-prompt-close]');
  }

  function enhanceHeroVideo() {
    var modal = document.querySelector('[data-hero-video-modal]');
    var video = modal && modal.querySelector('[data-hero-video]');
    var dialog = modal && modal.querySelector('[role="dialog"]');
    if (!modal || !video || !dialog) return;
    var previousFocus = null;

    function openVideo(trigger) {
      previousFocus = trigger || document.activeElement;
      document.dispatchEvent(new Event('kujo:close-mobile-menu'));
      modal.hidden = false;
      document.body.classList.add('modal-open');
      window.requestAnimationFrame(function () {
        var closeButton = modal.querySelector('.hero-video-modal__close');
        if (closeButton) closeButton.focus();
        else dialog.focus();
        var playRequest = video.play();
        if (playRequest && typeof playRequest.catch === 'function') playRequest.catch(function () {});
      });
    }

    function closeVideo() {
      video.pause();
      video.currentTime = 0;
      modal.hidden = true;
      document.body.classList.remove('modal-open');
      if (previousFocus && typeof previousFocus.focus === 'function') previousFocus.focus();
      previousFocus = null;
    }

    document.querySelectorAll('[data-hero-video-open]').forEach(function (button) {
      button.addEventListener('click', function () { openVideo(button); });
    });

    modal.querySelectorAll('[data-hero-video-close]').forEach(function (control) {
      control.addEventListener('click', closeVideo);
    });

    modal.addEventListener('keydown', function (event) {
      if (event.key === 'Escape') {
        event.preventDefault();
        closeVideo();
        return;
      }
      if (event.key !== 'Tab') return;
      var focusable = Array.prototype.slice.call(dialog.querySelectorAll('button, video[controls], a[href], [tabindex]:not([tabindex="-1"])'));
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

  function enhanceHeroDither() {
    var reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)');
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

    document.querySelectorAll('.home-hero__media, .page-hero__media, .tool-hero__media').forEach(function (media) {
      var image = media.querySelector('img');
      if (!image) return;

      var canvas = media.querySelector('[data-hero-dither]');
      if (!canvas) {
        canvas = document.createElement('canvas');
        canvas.className = 'hero-dither-canvas';
        canvas.dataset.heroDither = '';
        canvas.setAttribute('aria-hidden', 'true');
        media.appendChild(canvas);
      }

      var context = canvas.getContext('2d', { willReadFrequently: true });
      var sourceCanvas = document.createElement('canvas');
      var sourceContext = sourceCanvas.getContext('2d', { willReadFrequently: true });
      var sourceLuminance = null;
      var outputPixels = null;
      var frame = 0;
      var lastTick = 0;
      var resizeFrame = 0;
      var animationFrame = 0;
      var isReady = false;
      var isVisible = true;

      if (!context || !sourceContext) return;

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

        var sourcePixels = sourceContext.getImageData(0, 0, width, height).data;
        sourceLuminance = new Float32Array(width * height);
        for (var pixel = 0; pixel < sourceLuminance.length; pixel += 1) {
          var sourceIndex = pixel * 4;
          sourceLuminance[pixel] = (0.299 * sourcePixels[sourceIndex] + 0.587 * sourcePixels[sourceIndex + 1] + 0.114 * sourcePixels[sourceIndex + 2] - 128) * 1.12 + 128;
        }
        outputPixels = context.createImageData(width, height);
      }

      function drawFrame() {
        if (!sourceLuminance || !outputPixels) return;
        var width = canvas.width;
        var height = canvas.height;
        var target = outputPixels.data;
        var driftX = Math.floor(frame / 2) % 8;
        var driftY = Math.floor(frame / 3) % 8;
        var thresholdShift = reducedMotion.matches ? 0 : Math.sin(frame * 0.36) * 7;

        for (var y = 0; y < height; y += 1) {
          for (var x = 0; x < width; x += 1) {
            var pixelIndex = y * width + x;
            var targetIndex = pixelIndex * 4;
            var matrix = bayer8[(y + driftY) % 8][(x + driftX) % 8];
            var threshold = 94 + matrix * 1.88 + thresholdShift;
            var value = sourceLuminance[pixelIndex] > threshold ? 244 : 14;
            target[targetIndex] = value;
            target[targetIndex + 1] = value;
            target[targetIndex + 2] = value;
            target[targetIndex + 3] = 255;
          }
        }

        context.putImageData(outputPixels, 0, 0);
        canvas.dataset.ditherReady = 'true';
        canvas.dataset.ditherFrame = String(frame);
        frame += 1;
      }

      function stop() {
        if (!animationFrame) return;
        window.cancelAnimationFrame(animationFrame);
        animationFrame = 0;
      }

      function render(now) {
        animationFrame = 0;
        if (!isReady || !isVisible || document.hidden || reducedMotion.matches) return;
        if (now - lastTick >= 1000 / 14) {
          lastTick = now;
          drawFrame();
        }
        animationFrame = window.requestAnimationFrame(render);
      }

      function start() {
        if (animationFrame || !isReady || !isVisible || document.hidden || reducedMotion.matches) return;
        lastTick = 0;
        animationFrame = window.requestAnimationFrame(render);
      }

      function setup() {
        sizeCanvas();
        isReady = true;
        drawFrame();
        start();
      }

      function handleResize() {
        window.cancelAnimationFrame(resizeFrame);
        resizeFrame = window.requestAnimationFrame(function () {
          sizeCanvas();
          drawFrame();
        });
      }

      function handleVisibility() {
        if (document.hidden) stop();
        else start();
      }

      if ('IntersectionObserver' in window) {
        var visibilityObserver = new IntersectionObserver(function (entries) {
          entries.forEach(function (entry) {
            if (entry.target !== media) return;
            isVisible = entry.isIntersecting;
            if (isVisible) start();
            else stop();
          });
        });
        visibilityObserver.observe(media);
      }

      if (image.complete && image.naturalWidth) setup();
      else image.addEventListener('load', setup, { once: true });
      window.addEventListener('resize', handleResize);
      document.addEventListener('visibilitychange', handleVisibility);
      reducedMotion.addEventListener('change', function () {
        drawFrame();
        if (reducedMotion.matches) stop();
        else start();
      });
    });
  }

  function enhanceCarousels() {
    document.querySelectorAll('[data-carousel]').forEach(function (carousel) {
      var track = carousel.querySelector('[data-carousel-track]');
      var previous = carousel.querySelector('[data-carousel-previous]');
      var next = carousel.querySelector('[data-carousel-next]');
      if (!track || !previous || !next) return;

      function updateControls() {
        var maxScroll = Math.max(0, track.scrollWidth - track.clientWidth);
        previous.disabled = track.scrollLeft <= 2;
        next.disabled = track.scrollLeft >= maxScroll - 2;
      }

      function move(direction) {
        track.scrollBy({ left: direction * track.clientWidth, behavior: 'smooth' });
      }

      previous.addEventListener('click', function () { move(-1); });
      next.addEventListener('click', function () { move(1); });
      track.addEventListener('scroll', function () { window.requestAnimationFrame(updateControls); }, { passive: true });
      window.addEventListener('resize', updateControls);
      updateControls();
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
      if (!parent || !node.nodeValue.trim() || parent.closest(selector) || parent.closest('[data-scramble-skip], .ecosystem-carousel-controls')) return;
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

    document.querySelectorAll('h1, h2, .sk-badge, .eyebrow, .site-brand, .footer-wordmark').forEach(findMonoText);
  }

  function init() {
    enhanceCopyButtons();
    enhanceNavigationDropdowns();
    enhanceMobileNavigation();
    enhanceInstallModals();
    enhanceHeroVideo();
    enhanceHeroDither();
    enhanceCarousels();
    enhanceMonoScramble();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();

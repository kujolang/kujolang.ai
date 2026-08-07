(function () {
  'use strict';

  function enhanceCopyButtons() {
    document.querySelectorAll('[data-copy-code]').forEach(function (button) {
      button.addEventListener('click', function () {
        var code = button.closest('.sk-code-block');
        var text = code && code.querySelector('code');
        if (!text || !navigator.clipboard) return;
        navigator.clipboard.writeText(text.textContent.trim()).then(function () {
          var original = button.textContent;
          button.textContent = 'Copied';
          window.setTimeout(function () { button.textContent = original; }, 1600);
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

  function enhanceDitherHero() {
    var canvas = document.querySelector('[data-dither-canvas]');
    if (!canvas) return;

    var context = canvas.getContext('2d', { willReadFrequently: true });
    if (!context) return;

    var sourceCanvas = document.createElement('canvas');
    var sourceContext = sourceCanvas.getContext('2d', { willReadFrequently: true });
    var sourceData = null;
    var frame = 0;
    var lastTick = 0;
    var paused = document.hidden;
    var reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    var image = new Image();

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

    function deviceScale() {
      return Math.min(window.devicePixelRatio || 1, 2);
    }

    function sizeCanvas() {
      var dpr = deviceScale();
      var bounds = canvas.getBoundingClientRect();
      var width = Math.max(1, Math.floor(bounds.width * dpr));
      var height = Math.max(1, Math.floor(bounds.height * dpr));
      canvas.width = width;
      canvas.height = height;
      sourceCanvas.width = width;
      sourceCanvas.height = height;
    }

    function drawSource() {
      var width = sourceCanvas.width;
      var height = sourceCanvas.height;
      var imageWidth = image.naturalWidth;
      var imageHeight = image.naturalHeight;
      var scale = Math.max(width / imageWidth, height / imageHeight);
      var drawWidth = imageWidth * scale;
      var drawHeight = imageHeight * scale;
      var viewportRatio = window.innerWidth / window.innerHeight;
      var offsetX = (width - drawWidth) / 2;
      var offsetY = (height - drawHeight) / 2;

      if (viewportRatio >= 1.25) {
        offsetX -= width * 0.13;
        offsetY += height * 0.02;
      } else if (viewportRatio >= 0.75) {
        offsetX -= width * 0.05;
      } else {
        offsetX -= width * 0.22;
        offsetY += height * 0.02;
      }

      sourceContext.clearRect(0, 0, width, height);
      sourceContext.fillStyle = '#f9f9f9';
      sourceContext.fillRect(0, 0, width, height);
      sourceContext.drawImage(image, offsetX, offsetY, drawWidth, drawHeight);
      sourceData = sourceContext.getImageData(0, 0, width, height);
    }

    function paint() {
      if (!sourceData) return;
      var width = canvas.width;
      var height = canvas.height;
      var output = context.createImageData(width, height);
      var target = output.data;
      var source = sourceData.data;
      var dpr = deviceScale();
      var pixelScale = Math.max(1, Math.floor(2 * dpr));
      var driftX = Math.floor(frame / 2) % 8;
      var driftY = Math.floor(frame / 3) % 8;
      var thresholdShift = Math.sin(frame * 0.36) * 7;

      for (var y = 0; y < height; y += pixelScale) {
        var wave = Math.sin(y * 0.012) * 12 * dpr;
        var secondary = Math.sin(y * 0.02 - frame * 0.055) * 5 * dpr;
        for (var x = 0; x < width; x += pixelScale) {
          var sampleX = Math.max(0, Math.min(width - 1, Math.round(x + wave + secondary)));
          var sourceIndex = (y * width + sampleX) * 4;
          var luminance = 0.299 * source[sourceIndex] + 0.587 * source[sourceIndex + 1] + 0.114 * source[sourceIndex + 2];
          luminance = (luminance - 128) * 1.12 + 128;
          var matrix = bayer8[(Math.floor(y / pixelScale) + driftY) % 8][(Math.floor(x / pixelScale) + driftX) % 8];
          var value = luminance > 94 + matrix * 1.88 + thresholdShift ? 244 : 14;

          for (var blockY = 0; blockY < pixelScale; blockY += 1) {
            for (var blockX = 0; blockX < pixelScale; blockX += 1) {
              var pointX = x + blockX;
              var pointY = y + blockY;
              if (pointX >= width || pointY >= height) continue;
              var point = (pointY * width + pointX) * 4;
              target[point] = value;
              target[point + 1] = value;
              target[point + 2] = value;
              target[point + 3] = 255;
            }
          }
        }
      }

      context.putImageData(output, 0, 0);
      frame += 1;
    }

    function render(now) {
      if (!paused && now - lastTick >= 1000 / 14) {
        lastTick = now;
        paint();
      }
      if (!reduceMotion) window.requestAnimationFrame(render);
    }

    function setup() {
      sizeCanvas();
      drawSource();
      paint();
    }

    image.addEventListener('load', function () {
      setup();
      if (!reduceMotion) window.requestAnimationFrame(render);
    });

    document.addEventListener('visibilitychange', function () {
      paused = document.hidden;
    });

    var resizeTimer = 0;
    window.addEventListener('resize', function () {
      window.clearTimeout(resizeTimer);
      resizeTimer = window.setTimeout(setup, 120);
    });

    image.src = canvas.getAttribute('data-source');
  }

  function init() {
    enhanceCopyButtons();
    enhanceDrawerLinks();
    enhanceDitherHero();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();

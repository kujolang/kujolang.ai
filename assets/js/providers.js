(function () {
  'use strict';

  var grid = document.querySelector('[data-provider-grid]');
  var modal = document.querySelector('[data-provider-modal]');
  if (!grid || !modal) return;
  var records = [];
  var activeFilter = 'all';
  var previousFocus = null;
  var dialog = modal.querySelector('[role="dialog"]');
  var search = document.querySelector('[data-provider-search]');

  function copyText(text) {
    if (navigator.clipboard && window.isSecureContext) return navigator.clipboard.writeText(text);
    return new Promise(function (resolve, reject) {
      var helper = document.createElement('textarea');
      helper.value = text;
      helper.setAttribute('readonly', '');
      helper.style.position = 'fixed';
      helper.style.opacity = '0';
      document.body.appendChild(helper);
      helper.select();
      try { document.execCommand('copy') ? resolve() : reject(new Error('Copy failed')); } catch (error) { reject(error); } finally { helper.remove(); }
    });
  }

  function setCopiedState(button, status) {
    var copyLabel = button.dataset.copyLabel || 'Copy starter code';
    var copiedLabel = button.dataset.copiedLabel || 'Starter code copied';
    button.dataset.copied = 'true';
    button.setAttribute('aria-label', copiedLabel);
    if (status) status.textContent = 'Copied to clipboard.';
    window.setTimeout(function () {
      button.dataset.copied = 'false';
      button.setAttribute('aria-label', copyLabel);
      if (status) status.textContent = '';
    }, 1800);
  }

  function render() {
    var query = (search.value || '').toLowerCase().trim();
    var visible = records.filter(function (provider) {
      var matchesFilter = activeFilter === 'all' || provider.category.toLowerCase() === activeFilter;
      var haystack = [provider.name, provider.package, provider.protocol, provider.description].join(' ').toLowerCase();
      return matchesFilter && (!query || haystack.indexOf(query) !== -1);
    });
    grid.querySelectorAll('[data-provider-record]').forEach(function (card) {
      card.hidden = !visible.some(function (provider) { return provider.id === card.dataset.providerRecord; });
    });
    document.querySelector('[data-provider-count]').textContent = visible.length + ' provider' + (visible.length === 1 ? '' : 's');
  }

  function open(provider, trigger) {
    if (!provider) return;
    previousFocus = trigger || document.activeElement;
    modal.querySelector('[data-provider-logo]').src = provider.logo;
    modal.querySelector('[data-provider-logo]').alt = provider.name + ' logo';
    modal.querySelector('[data-provider-title]').textContent = provider.name;
    modal.querySelector('[data-provider-category]').textContent = provider.category + ' / ' + provider.package;
    modal.querySelector('[data-provider-description]').textContent = provider.description;
    modal.querySelector('[data-provider-protocol]').textContent = provider.protocol;
    modal.querySelector('[data-provider-package]').textContent = provider.package;
    modal.querySelector('[data-provider-code]').textContent = provider.code;
    modal.querySelector('[data-provider-install]').textContent = provider.install;
    modal.querySelector('[data-provider-repo]').href = provider.repo;
    modal.querySelector('[data-provider-docs]').href = provider.docs;
    modal.hidden = false;
    document.body.classList.add('modal-open');
    window.requestAnimationFrame(function () { dialog.focus(); });
  }

  function close() {
    modal.hidden = true;
    document.body.classList.remove('modal-open');
    if (previousFocus && typeof previousFocus.focus === 'function') previousFocus.focus();
    previousFocus = null;
  }

  fetch('/assets/data/providers.json').then(function (response) { if (!response.ok) throw new Error('Provider registry unavailable'); return response.json(); }).then(function (data) { records = data;
    document.querySelector('.providers-toolbar').hidden = false;
    grid.querySelectorAll('[data-provider-id]').forEach(function (button) {
      button.hidden = false;
      button.addEventListener('click', function () { open(records.find(function (item) { return item.id === button.dataset.providerId; }), button); });
    });
    render(); }).catch(function () { document.querySelector('[data-provider-count]').textContent = 'Starter details unavailable. Package links remain available.'; });
  search.addEventListener('input', render);
  document.querySelectorAll('[data-provider-filter]').forEach(function (button) { button.addEventListener('click', function () { activeFilter = button.dataset.providerFilter.toLowerCase(); document.querySelectorAll('[data-provider-filter]').forEach(function (item) { var active = item === button; item.classList.toggle('is-active', active); item.setAttribute('aria-pressed', String(active)); }); render(); }); });
  modal.querySelectorAll('[data-provider-close]').forEach(function (control) { control.addEventListener('click', close); });
  modal.addEventListener('keydown', function (event) {
    if (event.key === 'Escape') { event.preventDefault(); close(); return; }
    if (event.key !== 'Tab') return;
    var focusable = Array.prototype.slice.call(dialog.querySelectorAll('button, a[href], [tabindex]:not([tabindex="-1"])'));
    if (!focusable.length) return;
    if (event.shiftKey && document.activeElement === focusable[0]) { event.preventDefault(); focusable[focusable.length - 1].focus(); }
    else if (!event.shiftKey && document.activeElement === focusable[focusable.length - 1]) { event.preventDefault(); focusable[0].focus(); }
  });
  modal.querySelector('[data-provider-copy]').addEventListener('click', function (event) {
    var button = event.currentTarget;
    var status = modal.querySelector('[data-provider-copy-status]');
    copyText(modal.querySelector('[data-provider-code]').textContent).then(function () { setCopiedState(button, status); }).catch(function () { status.textContent = 'Copy failed. Select the code to copy it.'; });
  });
}());

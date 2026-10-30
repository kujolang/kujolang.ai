const esc=s=>String(s).replaceAll('&','&amp;').replaceAll('<','&lt;').replaceAll('>','&gt;').replaceAll('"','&quot;');
function highlight(code){
 // Match comments/strings first so keywords inside them retain their own token class.
 const tokens=/("(?:\\.|[^"\\])*"|#[^\n]*|\/\/[^\n]*|\b(?:func|let|mut|return|if|else|for|in|async|await|struct|enum|match|case|try|except|throw|yield|import|from|test)\b|\b(?:true|false|null)\b|\b\d+(?:\.\d+)?\b)/g;
 return code.split(tokens).map((value,i)=>{
  if(i%2===0)return esc(value);
  const kind=value.startsWith('"')?'string':value.startsWith('#')||value.startsWith('//')?'comment':/^\d/.test(value)?'number':['true','false','null'].includes(value)?'literal':'keyword';
  return `<span class="syntax-token syntax-${kind}">${esc(value)}</span>`;
 }).join('');
}
export function block(code,syntax=true){return `<div class="sample-code"><pre tabindex="0"><code>${syntax?highlight(code):esc(code)}</code></pre><button type="button" class="sk-button code-copy-icon" data-copy-code aria-label="Copy code" title="Copy code" hidden><svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><rect x="8" y="8" width="12" height="12" rx="1.5"/><path d="M16 8V4H4v12h4"/></svg></button><span role="status" data-code-status></span></div>`;}

(function(){
  var WA='919978791167', MAIL='sales@gujaratbio.com';
  /* Paste your Google Apps Script web-app URL (or n8n webhook URL) here. Leave empty to skip lead logging. */
  var LEAD_ENDPOINT='';

  /* first-touch attribution: remember where the visitor came from */
  function store(k,v){try{localStorage.setItem(k,v)}catch(e){}}
  function load(k){try{return localStorage.getItem(k)||''}catch(e){return ''}}
  (function(){
    var q=new URLSearchParams(location.search), keys=['utm_source','utm_medium','utm_campaign','utm_content','utm_term','src','article'];
    keys.forEach(function(k){if(q.get(k)&&!load('gbo_'+k))store('gbo_'+k,q.get(k))});
    if(!load('gbo_ref')&&document.referrer&&document.referrer.indexOf(location.host)<0)store('gbo_ref',document.referrer);
    if(!load('gbo_landing'))store('gbo_landing',location.pathname);
  })();
  function logLead(data){
    if(!LEAD_ENDPOINT)return;
    var keys=['utm_source','utm_medium','utm_campaign','utm_content','utm_term','src','article','ref','landing'];
    keys.forEach(function(k){data[k]=load('gbo_'+k)});
    data.page=location.href; data.site=location.host;
    try{data.timezone=Intl.DateTimeFormat().resolvedOptions().timeZone}catch(e){}
    try{fetch(LEAD_ENDPOINT,{method:'POST',mode:'no-cors',keepalive:true,headers:{'Content-Type':'text/plain'},body:JSON.stringify(data)})}catch(e){}
  }
  var nav=document.getElementById('nav'), mb=document.getElementById('menu-btn');
  if(mb&&nav){mb.addEventListener('click',function(){var o=nav.classList.toggle('open');mb.setAttribute('aria-expanded',o)})}

  /* enquiry forms -> WhatsApp or email */
  function collect(form){
    var lines=[], t=form.getAttribute('data-subject')||'Website enquiry';
    lines.push('Hello Gujarat Bio Organics, '+t+'.');
    Array.prototype.forEach.call(form.elements,function(el){
      if(!el.name||el.type==='submit'||el.type==='button')return;
      var v=(el.value||'').trim(); if(!v)return;
      lines.push((el.getAttribute('data-label')||el.name)+': '+v);
    });
    var sel=window.__selected&&window.__selected();
    if(sel&&sel.length){lines.push('Grades requested:');sel.forEach(function(s){lines.push('- '+s)})}
    return lines.join('\n');
  }
  Array.prototype.forEach.call(document.querySelectorAll('form[data-enquiry]'),function(form){
    form.addEventListener('submit',function(e){
      e.preventDefault();
      if(!form.checkValidity()){form.reportValidity();return}
      var mode=(e.submitter&&e.submitter.getAttribute('data-mode'))||'wa', msg=collect(form);
      var d={form:form.getAttribute('data-subject')||'Website enquiry',channel:mode,message:msg};
      Array.prototype.forEach.call(form.elements,function(el){if(el.name&&el.type!=='submit'&&el.type!=='button'&&(el.value||'').trim())d[el.name]=el.value.trim()});
      var sg=window.__selected&&window.__selected(); if(sg&&sg.length)d.grades=sg.join('; ');
      logLead(d);
      if(mode==='mail'){location.href='mailto:'+MAIL+'?subject='+encodeURIComponent(form.getAttribute('data-subject')||'Website enquiry')+'&body='+encodeURIComponent(msg)}
      else{window.open('https://wa.me/'+WA+'?text='+encodeURIComponent(msg),'_blank','noopener')}
    });
  });

  /* grade explorer */
  var table=document.getElementById('grades');
  if(table){
    var rows=Array.prototype.slice.call(table.querySelectorAll('tbody tr'));
    var chips=Array.prototype.slice.call(document.querySelectorAll('.chip'));
    var bar=document.getElementById('bar'), count=document.getElementById('bar-count');
    function apply(g){
      chips.forEach(function(c){c.setAttribute('aria-pressed',String(c.getAttribute('data-g')===g))});
      rows.forEach(function(r){r.hidden=!(g==='all'||r.getAttribute('data-g')===g)});
      if(history.replaceState)history.replaceState(null,'',g==='all'?location.pathname:'#'+g);
    }
    chips.forEach(function(c){c.addEventListener('click',function(){apply(c.getAttribute('data-g'))})});
    function selected(){return rows.filter(function(r){return r.querySelector('input').checked}).map(function(r){return r.getAttribute('data-name')+' ('+r.getAttribute('data-form')+')'})}
    window.__selected=selected;
    function upd(){var n=selected().length;count.textContent=n+(n===1?' grade selected':' grades selected');bar.classList.toggle('on',n>0);document.body.classList.toggle('has-bar',n>0)}
    rows.forEach(function(r){r.querySelector('input').addEventListener('change',upd)});
    document.getElementById('bar-clear').addEventListener('click',function(){rows.forEach(function(r){r.querySelector('input').checked=false});upd()});
    document.getElementById('bar-send').addEventListener('click',function(){
      var m='Hello Gujarat Bio Organics, please send a quote for these grades:\n'+selected().map(function(s){return '- '+s}).join('\n')+'\n\nQuantity and destination: ';
      logLead({form:'Grade selection',channel:'wa',grades:selected().join('; '),message:m});
      window.open('https://wa.me/'+WA+'?text='+encodeURIComponent(m),'_blank','noopener');
    });
    var h=(location.hash||'').replace('#','');
    apply(chips.some(function(c){return c.getAttribute('data-g')===h})?h:'all');
  }
  var y=document.getElementById('yr'); if(y)y.textContent=new Date().getFullYear();
})();

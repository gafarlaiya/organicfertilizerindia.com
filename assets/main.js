(function(){
  var WA='919978791167', MAIL='sales@gujaratbio.com';
  /* Lead database (Supabase). The key below is the public publishable key: it can only ADD leads, never read them. */
  var SB_URL='https://filbmvtclfcrrvxckema.supabase.co', SB_KEY='sb_publishable_qbndsVEhemxGLYZa6P3PyQ_iDNmsmmT';

  /* first-touch attribution: remember where the visitor came from */
  function store(k,v){try{localStorage.setItem(k,v)}catch(e){}}
  function load(k){try{return localStorage.getItem(k)||''}catch(e){return ''}}
  (function(){
    var q=new URLSearchParams(location.search), keys=['utm_source','utm_medium','utm_campaign','utm_content','utm_term','src','article'];
    keys.forEach(function(k){if(q.get(k)&&!load('gbo_'+k))store('gbo_'+k,q.get(k))});
    if(!load('gbo_ref')&&document.referrer&&document.referrer.indexOf(location.host)<0)store('gbo_ref',document.referrer);
    if(!load('gbo_landing'))store('gbo_landing',location.pathname);
  })();
  function logLead(d){
    if(!SB_URL||!SB_KEY)return;
    var row={
      name:d.name,company:d.company||d.shop||d.brand,phone:d.phone,email:d.email,country:d.country||d.place,
      interest:d.interest||d.product||d.type||d.crops,grades:d.grades,qty:d.qty||d.volume,destination:d.dest,
      form:d.form,channel:d.channel,message:d.message,
      utm_source:load('gbo_utm_source')||load('gbo_src'),utm_medium:load('gbo_utm_medium'),utm_campaign:load('gbo_utm_campaign'),
      utm_content:load('gbo_utm_content'),utm_term:load('gbo_utm_term'),article:load('gbo_article'),
      referrer:load('gbo_ref'),landing:load('gbo_landing'),page:location.href,site:location.host
    };
    try{row.timezone=Intl.DateTimeFormat().resolvedOptions().timeZone}catch(e){}
    try{fetch(SB_URL+'/rest/v1/leads',{method:'POST',keepalive:true,headers:{'apikey':SB_KEY,'Content-Type':'application/json','Prefer':'return=minimal'},body:JSON.stringify(row)}).catch(function(){})}catch(e){}
  }

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

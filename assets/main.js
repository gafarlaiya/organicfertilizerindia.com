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
    if(!SB_URL||!SB_KEY)return Promise.resolve(false);
    var row={
      name:d.name,company:d.company||d.shop||d.brand,phone:d.phone,email:d.email,country:d.country||d.place,
      interest:d.interest||d.product||d.type||d.crops,grades:d.grades,qty:d.qty||d.volume,destination:d.dest,
      form:d.form,channel:d.channel,message:d.message,
      utm_source:load('gbo_utm_source')||load('gbo_src'),utm_medium:load('gbo_utm_medium'),utm_campaign:load('gbo_utm_campaign'),
      utm_content:load('gbo_utm_content'),utm_term:load('gbo_utm_term'),article:load('gbo_article'),
      referrer:load('gbo_ref'),landing:load('gbo_landing'),page:location.href,site:location.host
    };
    try{row.timezone=Intl.DateTimeFormat().resolvedOptions().timeZone}catch(e){}
    var ctl=window.AbortController?new AbortController():null, t=setTimeout(function(){if(ctl)ctl.abort()},10000);
    return fetch(SB_URL+'/rest/v1/leads',{method:'POST',keepalive:true,signal:ctl?ctl.signal:undefined,headers:{'apikey':SB_KEY,'Content-Type':'application/json','Prefer':'return=minimal'},body:JSON.stringify(row)})
      .then(function(r){clearTimeout(t);return r.ok}).catch(function(){clearTimeout(t);return false});
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
  function esc(v){return String(v).replace(/[&<>"']/g,function(c){return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]})}
  Array.prototype.forEach.call(document.querySelectorAll('form[data-enquiry]'),function(form){
    var btn=form.querySelector('button[type=submit]'), msg=form.querySelector('.form-msg'), label=btn?btn.textContent:'';
    form.addEventListener('submit',function(e){
      e.preventDefault();
      if(!form.checkValidity()){form.reportValidity();return}
      var hp=form.elements['website']; if(hp&&hp.value){return} /* spam trap */
      var text=collect(form);
      var d={form:form.getAttribute('data-subject')||'Website enquiry',channel:'website',message:text};
      Array.prototype.forEach.call(form.elements,function(el){if(el.name&&el.name!=='website'&&el.type!=='submit'&&el.type!=='button'&&(el.value||'').trim())d[el.name]=el.value.trim()});
      var sg=window.__selected&&window.__selected(); if(sg&&sg.length)d.grades=sg.join('; ');
      if(btn){btn.disabled=true;btn.textContent='Sending...'} if(msg){msg.textContent='';msg.className='form-msg'}
      var wa='https://wa.me/'+WA+'?text='+encodeURIComponent(text);
      logLead(d).then(function(ok){
        var box=form.parentNode;
        if(ok){
          box.innerHTML='<div class="thanks" role="status"><h3>Thank you'+(d.name?', '+esc(d.name.split(' ')[0]):'')+'. We have your enquiry.</h3><p>Our team will reply within one working day'+(d.email?' at '+esc(d.email):' on the number you gave')+'. You do not need to do anything else.</p><div class="form-actions"><a class="btn btn-wa" target="_blank" rel="noopener" href="'+wa+'">Want a faster reply? Chat on WhatsApp</a></div></div>';
          try{sessionStorage.removeItem('gbo_grades')}catch(x){}
          box.scrollIntoView({behavior:'smooth',block:'center'});
        }else{
          if(btn){btn.disabled=false;btn.textContent=label}
          if(msg){msg.className='form-msg err';msg.innerHTML='We could not send this just now. Please try again, or <a target="_blank" rel="noopener" href="'+wa+'">send it on WhatsApp</a> or email <a href="mailto:'+MAIL+'?subject='+encodeURIComponent(d.form)+'&body='+encodeURIComponent(text)+'">'+MAIL+'</a>.'}
        }
      });
    });
    /* grades picked on the products page are carried into the quote form */
    var gf=form.elements['grades'], saved=null; try{saved=sessionStorage.getItem('gbo_grades')}catch(x){}
    if(gf&&saved&&!gf.value)gf.value=saved;
  });

  /* grade explorer */
  var table=document.getElementById('grades');
  if(table&&table.tagName==='TABLE'&&document.getElementById('bar')){
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
      try{sessionStorage.setItem('gbo_grades',selected().join('\n'))}catch(x){}
      location.href='/bulk-supply/#enquiry';
    });
    var h=(location.hash||'').replace('#','');
    apply(chips.some(function(c){return c.getAttribute('data-g')===h})?h:'all');
  }
  document.addEventListener('click',function(e){
    var b=e.target.closest&&e.target.closest('button.yt');if(!b)return;
    var f=document.createElement('iframe');f.src='https://www.youtube-nocookie.com/embed/'+encodeURIComponent(b.getAttribute('data-id'))+'?autoplay=1&rel=0';
    f.allow='autoplay; encrypted-media; picture-in-picture';f.allowFullscreen=true;f.title=b.getAttribute('aria-label')||'Video';
    b.replaceChildren(f);b.removeAttribute('aria-label');
  });
  var y=document.getElementById('yr'); if(y)y.textContent=new Date().getFullYear();
})();

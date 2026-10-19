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
  /* ad click IDs: kept only when the visitor has not declined cookies */
  function consented(){return window.GBO_CONSENT==='granted'}
  function clickIds(){
    if(!consented())return;
    var q=new URLSearchParams(location.search);
    ['gclid','fbclid'].forEach(function(k){if(q.get(k)){store('gbo_'+k,q.get(k));if(k==='fbclid')store('gbo_fbclid_ts',String(Date.now()))}});
  }
  clickIds();

  /* event layer: one dataLayer push per event. GTM reads it; without GTM the same event goes straight to GA4. */
  var DL=window.dataLayer=window.dataLayer||[];
  function track(n,p){
    var o={event:n},k; if(p)for(k in p)if(p[k]!==undefined&&p[k]!==null&&p[k]!=='')o[k]=p[k];
    o.page_type=window.GBO_PT;
    DL.push(o);
    if(!window.GBO_GTM&&window.gtag){var a={};for(k in o)if(k!=='event')a[k]=o[k];try{gtag('event',n,a)}catch(e){}}
  }
  function uid(){return (window.crypto&&crypto.randomUUID)?crypto.randomUUID():'e'+Date.now().toString(36)+Math.random().toString(36).slice(2,10)}
  function ck(n){var m=document.cookie.match(new RegExp('(?:^|; )'+n+'=([^;]*)'));return m?decodeURIComponent(m[1]):''}
  function attr(){
    var ga=ck('_ga').split('.'), fbc=ck('_fbc'), id=load('gbo_fbclid');
    if(!fbc&&id)fbc='fb.1.'+(load('gbo_fbclid_ts')||Date.now())+'.'+id;
    return {gclid:load('gbo_gclid'),fbclid:id,fbp:ck('_fbp'),fbc:fbc,ga_client_id:ga.length>=4?ga[2]+'.'+ga[3]:'',consent:window.GBO_CONSENT||''};
  }
  window.gboTrack=track;window.gboUid=uid;window.gboAttr=attr;

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
    var base=JSON.parse(JSON.stringify(row)), at=attr(), k;
    for(k in at)if(at[k])row[k]=at[k];
    if(d.event_id)row.event_id=d.event_id;
    function post(rw){
      var ctl=window.AbortController?new AbortController():null, t=setTimeout(function(){if(ctl)ctl.abort()},10000);
      return fetch(SB_URL+'/rest/v1/leads',{method:'POST',keepalive:true,signal:ctl?ctl.signal:undefined,headers:{'apikey':SB_KEY,'Content-Type':'application/json','Prefer':'return=minimal'},body:JSON.stringify(rw)})
        .then(function(r){clearTimeout(t);return r}).catch(function(){clearTimeout(t);return null});
    }
    /* if the database rejects the extra tracking fields, still save the lead without them */
    return post(row).then(function(r){
      if(r&&r.ok)return true;
      if(r&&r.status>=400&&r.status<500)return post(base).then(function(r2){return !!(r2&&r2.ok)});
      return false;
    });
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
    var started=false;
    form.addEventListener('focusin',function(){if(!started){started=true;track('form_start',{form_name:form.getAttribute('data-subject')||'Website enquiry'})}});
    form.addEventListener('submit',function(e){
      e.preventDefault();
      if(!form.checkValidity()){form.reportValidity();return}
      var hp=form.elements['website']; if(hp&&hp.value){return} /* spam trap */
      var text=collect(form);
      var d={form:form.getAttribute('data-subject')||'Website enquiry',channel:'website',message:text};
      Array.prototype.forEach.call(form.elements,function(el){if(el.name&&el.name!=='website'&&el.type!=='submit'&&el.type!=='button'&&(el.value||'').trim())d[el.name]=el.value.trim()});
      var sg=window.__selected&&window.__selected(); if(sg&&sg.length)d.grades=sg.join('; ');
      d.event_id=uid();
      if(btn){btn.disabled=true;btn.textContent='Sending...'} if(msg){msg.textContent='';msg.className='form-msg'}
      var wa='https://wa.me/'+WA+'?text='+encodeURIComponent(text);
      logLead(d).then(function(ok){
        var box=form.parentNode;
        if(ok){
          track('generate_lead',{form_name:d.form,lead_channel:'website_form',event_id:d.event_id,grades_count:sg?sg.length:0});
          box.innerHTML='<div class="thanks" role="status"><h3>Thank you'+(d.name?', '+esc(d.name.split(' ')[0]):'')+'. We have your enquiry.</h3><p>Our team will reply within one working day'+(d.email?' at '+esc(d.email):' on the number you gave')+'. You do not need to do anything else.</p><div class="form-actions"><a class="btn btn-wa" target="_blank" rel="noopener" href="'+wa+'">Want a faster reply? Chat on WhatsApp</a></div></div>';
          try{sessionStorage.removeItem('gbo_grades')}catch(x){}
          box.scrollIntoView({behavior:'smooth',block:'center'});
        }else{
          track('form_error',{form_name:d.form});
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
      track('begin_quote',{grades_count:selected().length});
      try{sessionStorage.setItem('gbo_grades',selected().join('\n'))}catch(x){}
      location.href='/bulk-supply/#enquiry';
    });
    var h=(location.hash||'').replace('#','');
    apply(chips.some(function(c){return c.getAttribute('data-g')===h})?h:'all');
  }
  document.addEventListener('click',function(e){
    var b=e.target.closest&&e.target.closest('button.yt');if(!b)return;
    track('video_start',{video_id:b.getAttribute('data-id'),video_provider:'youtube',video_title:(b.getAttribute('aria-label')||'').replace(/^Play video: /,'')});
    var f=document.createElement('iframe');f.src='https://www.youtube-nocookie.com/embed/'+encodeURIComponent(b.getAttribute('data-id'))+'?autoplay=1&rel=0';
    f.allow='autoplay; encrypted-media; picture-in-picture';f.allowFullscreen=true;f.title=b.getAttribute('aria-label')||'Video';
    b.replaceChildren(f);b.removeAttribute('aria-label');
  });
  var co=document.getElementById('chat-open');
  if(co){co.addEventListener('click',function(){
    if(window.GBOChat){window.GBOChat.open();return}
    var s=document.createElement('script');s.src='/assets/chat.js?v='+(window.GBO_CHAT_V||'1');s.onload=function(){window.GBOChat&&window.GBOChat.open()};document.head.appendChild(s);
  })}
  /* click tracking: WhatsApp, phone, email */
  function where(a){
    if(a.classList.contains('wa-float'))return 'floating_button';
    if(a.closest('.chat'))return 'chat';
    if(a.closest('.site-footer'))return 'footer';
    if(a.closest('.site-header'))return 'header';
    if(a.closest('.thanks'))return 'form_thanks';
    if(a.closest('.cta'))return 'cta_band';
    if(a.closest('.form-box'))return 'form';
    return 'content';
  }
  document.addEventListener('click',function(e){
    var a=e.target.closest&&e.target.closest('a[href]');if(!a)return;
    var h=a.getAttribute('href')||'', n='';
    if(/^https?:\/\/(wa\.me|api\.whatsapp\.com)\//.test(h))n='click_whatsapp';
    else if(h.indexOf('tel:')===0)n='click_phone';
    else if(h.indexOf('mailto:')===0)n='click_email';
    if(n)track(n,{link_location:where(a),link_text:(a.textContent||'').trim().slice(0,60),event_id:uid()});
  });

  /* cookie choice */
  function setConsent(v){
    store('gbo_consent',v);window.GBO_CONSENT=v;
    var s={ad_storage:v,ad_user_data:v,ad_personalization:v,analytics_storage:v};
    if(window.gtag)gtag('consent','update',s);
    DL.push({event:'gbo_consent_update',consent:v});
    if(v==='granted')clickIds();
    var b=document.getElementById('ck');if(b)b.remove();
  }
  function banner(){
    if(document.getElementById('ck'))return;
    var b=document.createElement('div');b.id='ck';b.className='ck';b.setAttribute('role','dialog');b.setAttribute('aria-label','Cookie choices');
    b.innerHTML='<p>We use cookies to see which pages help visitors and to measure our advertising. You can accept or decline; the site works either way. <a href="/privacy-policy">Privacy and cookies</a></p><div><button type="button" class="btn btn-primary" data-ck="granted">Accept</button><button type="button" class="btn btn-ghost" data-ck="denied">Decline</button></div>';
    document.body.appendChild(b);
  }
  document.addEventListener('click',function(e){
    var c=e.target.closest&&e.target.closest('[data-ck]');if(c){setConsent(c.getAttribute('data-ck'));return}
    if(e.target.closest&&e.target.closest('[data-cookie-settings]'))banner();
  });
  if(window.GBO_NEEDS_CHOICE)banner();
  if(window.GBO_PT==='404')track('page_not_found',{page_path:location.pathname});

  var y=document.getElementById('yr'); if(y)y.textContent=new Date().getFullYear();
})();

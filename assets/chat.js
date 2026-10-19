(function(){
  if(window.GBOChat)return;
  var EP='https://filbmvtclfcrrvxckema.supabase.co/functions/v1/sales-chat', WA='https://wa.me/919978791167';
  var KEY='sb_publishable_qbndsVEhemxGLYZa6P3PyQ_iDNmsmmT';
  function ld(k){try{return localStorage.getItem(k)||''}catch(e){return ''}}
  function ss(k,v){try{if(v===undefined)return sessionStorage.getItem(k)||'';sessionStorage.setItem(k,v)}catch(e){return ''}}
  var sid=ss('gbo_chat_sid');
  if(!sid){sid='s'+Math.random().toString(36).slice(2,12)+Date.now().toString(36);ss('gbo_chat_sid',sid)}
  var hist=[];try{hist=JSON.parse(ss('gbo_chat_hist')||'[]')}catch(e){}
  var busy=false, built=false, box, log, input, send, chips;

  function el(t,c,txt){var e=document.createElement(t);if(c)e.className=c;if(txt)e.textContent=txt;return e}
  function addText(node,text){
    var re=/(https?:\/\/[^\s<>"')]+[^\s<>"').,;:!?])/g, last=0, m;
    while((m=re.exec(text))){
      if(m.index>last)node.appendChild(document.createTextNode(text.slice(last,m.index)));
      var a=el('a','',m[1].replace(/^https?:\/\/(www\.)?/,'').replace(/\/$/,''));a.href=m[1];a.rel='noopener';
      if(m[1].indexOf('b2b.gujaratbio.com')<0)a.target='_blank';
      node.appendChild(a);last=m.index+m[1].length;
    }
    if(last<text.length)node.appendChild(document.createTextNode(text.slice(last)));
  }
  function bubble(role,text){
    var b=el('div','cb '+(role==='user'?'cb-u':'cb-a'));
    text.split(/\n{2,}/).forEach(function(p){var pe=el('p');addText(pe,p);b.appendChild(pe)});
    log.appendChild(b);log.scrollTop=log.scrollHeight;return b;
  }
  function save(){try{ss('gbo_chat_hist',JSON.stringify(hist.slice(-30)))}catch(e){}}
  function build(){
    if(built)return;built=true;
    box=el('section','chat');box.id='chat-panel';box.setAttribute('role','dialog');box.setAttribute('aria-label','Chat with Gujarat Bio Organics');
    var head=el('div','chat-h');
    var t=el('div','chat-t');t.appendChild(el('strong','','Gujarat Bio Organics'));t.appendChild(el('span','','Sales assistant (AI). Replies in your language.'));
    var wa=el('a','chat-wa','Talk to a person');wa.href=WA;wa.rel='noopener';
    var x=el('button','chat-x','×');x.type='button';x.setAttribute('aria-label','Close chat');x.addEventListener('click',close);
    head.appendChild(t);head.appendChild(wa);head.appendChild(x);
    log=el('div','chat-l');log.setAttribute('role','log');log.setAttribute('aria-live','polite');
    chips=el('div','chat-c');
    ['I am an importer','Private label / OEM','Bulk supply','I am a grower'].forEach(function(c){
      var b=el('button','',c);b.type='button';b.addEventListener('click',function(){submit(c)});chips.appendChild(b)});
    var form=el('form','chat-f');input=el('input');input.type='text';input.maxLength=1000;input.placeholder='Type your question';input.setAttribute('aria-label','Your message');input.autocomplete='off';
    send=el('button','chat-s','Send');send.type='submit';form.appendChild(input);form.appendChild(send);
    form.addEventListener('submit',function(e){e.preventDefault();var v=input.value.trim();if(v)submit(v)});
    box.appendChild(head);box.appendChild(log);box.appendChild(chips);box.appendChild(form);
    box.addEventListener('keydown',function(e){if(e.key==='Escape')close()});
    document.body.appendChild(box);
    if(hist.length){hist.forEach(function(m){bubble(m.r,m.t)});chips.style.display='none'}
    else bubble('assistant','Hello, I am the Gujarat Bio Organics sales assistant. Tell me what you are looking for and I will help, or get you a quote and a free sample. No minimum order.');
  }
  function submit(text){
    if(busy)return;busy=true;chips.style.display='none';input.value='';
    bubble('user',text);hist.push({r:'user',t:text});save();
    send.disabled=true;var typing=el('div','cb cb-a cb-t');typing.setAttribute('aria-label','Typing');typing.appendChild(el('i'));typing.appendChild(el('i'));typing.appendChild(el('i'));log.appendChild(typing);log.scrollTop=log.scrollHeight;
    var ctx={utm_source:ld('gbo_utm_source')||ld('gbo_src'),utm_medium:ld('gbo_utm_medium'),utm_campaign:ld('gbo_utm_campaign'),utm_content:ld('gbo_utm_content'),utm_term:ld('gbo_utm_term'),article:ld('gbo_article'),referrer:ld('gbo_ref'),landing:ld('gbo_landing')};
    try{ctx.timezone=Intl.DateTimeFormat().resolvedOptions().timeZone}catch(e){}
    var at=window.gboAttr?window.gboAttr():{};
    ['gclid','fbclid','fbp','fbc','ga_client_id','consent'].forEach(function(k){if(at[k])ctx[k]=at[k]});
    ctx.event_id='chat_'+sid;
    if(!ss('gbo_chat_started')){ss('gbo_chat_started','1');if(window.gboTrack)gboTrack('chat_start')}
    var ctl=window.AbortController?new AbortController():null,tm=setTimeout(function(){if(ctl)ctl.abort()},50000);
    fetch(EP,{method:'POST',signal:ctl?ctl.signal:undefined,headers:{'Content-Type':'application/json','apikey':KEY},body:JSON.stringify({session_id:sid,message:text,page:location.pathname,ctx:ctx})})
      .then(function(r){return r.json()}).then(function(d){
        clearTimeout(tm);typing.remove();var rep=d&&d.reply?d.reply:'Sorry, something went wrong. Please message us on WhatsApp: '+WA;
        bubble('assistant',rep);hist.push({r:'assistant',t:rep});save();
        if(d&&d.lead_saved&&!ss('gbo_chat_lead')){ss('gbo_chat_lead','1');if(window.gboTrack)gboTrack('generate_lead',{form_name:'chatbot',lead_channel:'chatbot',event_id:'chat_'+sid})}
      }).catch(function(){
        clearTimeout(tm);typing.remove();bubble('assistant','I could not connect just now. Please message our team on WhatsApp: '+WA);
      }).then(function(){busy=false;send.disabled=false;input.focus()});
  }
  var launcher=document.getElementById('chat-open');
  var opened=false;
  function open(){if(!opened){opened=true;if(window.gboTrack)gboTrack('chat_open')}build();box.classList.add('on');if(launcher)launcher.setAttribute('aria-expanded','true');setTimeout(function(){input.focus()},50)}
  function close(){if(box)box.classList.remove('on');if(launcher){launcher.setAttribute('aria-expanded','false');launcher.focus()}}
  window.GBOChat={open:open,close:close};
})();

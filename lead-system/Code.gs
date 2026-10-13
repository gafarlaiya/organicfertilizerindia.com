/**
 * Gujarat Bio Organics - lead capture
 * Receives website form posts, saves them to the "Leads" tab,
 * scores them, and emails you an alert.
 *
 * SETUP (5 minutes): see SETUP.md
 */
var OWNER_EMAIL = 'sales@gujaratbio.com';   // alerts go here
var SHEET_NAME  = 'Leads';

var HEADERS = ['Received','Lead ID','Stage','Score','Priority','Next follow-up','Owner',
  'Name','Company','Phone / WhatsApp','Email','Country / Place','Interest / Product','Grades','Quantity / Volume',
  'Destination','Form','Channel','Source','Medium','Campaign','Article','Referrer','Landing page','Page','Site','Timezone','Message','Notes'];

function doPost(e) {
  var d = {};
  try { d = JSON.parse(e.postData.contents); } catch (err) { return out('bad json'); }
  var sh = sheet_();
  var id = 'GBO-' + Utilities.formatDate(new Date(), 'Asia/Kolkata', 'yyMMdd') + '-' + String(sh.getLastRow()).padStart(3, '0');
  var s = score_(d);
  var row = [new Date(), id, 'New', s.score, s.priority, followup_(s.priority), '',
    d.name||'', d.company||d.shop||d.brand||'', "'" + (d.phone||''), d.email||'',
    d.country||d.place||'', d.interest||d.product||d.type||d.crops||'', d.grades||'', d.qty||d.volume||'',
    d.dest||'', d.form||'', d.channel||'', d.utm_source||d.src||'', d.utm_medium||'', d.utm_campaign||'',
    d.article||'', d.ref||'', d.landing||'', d.page||'', d.site||'', d.timezone||'', d.message||'', ''];
  sh.appendRow(row);
  alert_(id, s, d);
  return out('ok');
}

function doGet() { return out('lead endpoint running'); }

function sheet_() {
  var ss = SpreadsheetApp.getActiveSpreadsheet();
  var sh = ss.getSheetByName(SHEET_NAME) || ss.insertSheet(SHEET_NAME);
  if (sh.getLastRow() === 0) {
    sh.appendRow(HEADERS);
    sh.setFrozenRows(1);
    sh.getRange(1,1,1,HEADERS.length).setFontWeight('bold').setBackground('#1f5c3a').setFontColor('#ffffff');
    var stages = SpreadsheetApp.newDataValidation().requireValueInList(
      ['New','Contacted','Qualified','Sample sent','Quote sent','Negotiation','Won','Lost','Nurture'], true).build();
    sh.getRange(2,3,1000,1).setDataValidation(stages);
  }
  return sh;
}

/* Simple, transparent scoring: edit the numbers to suit you */
function score_(d) {
  var s = 0, t = JSON.stringify(d).toLowerCase();
  var type = ((d.type||'') + ' ' + (d.form||'')).toLowerCase();
  if (/export|import/.test(type)) s += 30;
  else if (/private|oem|label/.test(type)) s += 30;
  else if (/bulk/.test(type)) s += 25;
  else if (/distribut|dealer/.test(type)) s += 20;
  var q = parseFloat(String(d.qty||d.volume||'').replace(/[^0-9.]/g,'')) || 0;
  if (/container|fcl|ton|mt|kg/.test(String(d.qty||d.volume||'').toLowerCase()) || q >= 1) s += 15;
  if (q >= 10 || /container|fcl/.test(t)) s += 15;
  if (d.email && !/gmail|yahoo|hotmail|outlook/.test(d.email.toLowerCase())) s += 10;
  if (d.company) s += 10;
  if (d.phone) s += 10;
  if (d.grades) s += 10;
  var india = /india|gujarat|maharashtra|punjab|up |uttar/.test(String(d.country||d.place||'').toLowerCase());
  if (d.country && !india) s += 10;
  var priority = s >= 60 ? 'Hot' : (s >= 35 ? 'Warm' : 'Cold');
  return {score: s, priority: priority};
}

function followup_(p) {
  var days = p === 'Hot' ? 0 : (p === 'Warm' ? 1 : 3);
  return new Date(Date.now() + days * 86400000);
}

function alert_(id, s, d) {
  var body = ['New ' + s.priority + ' lead (' + s.score + ' pts): ' + id, '',
    'Form: ' + (d.form||''), 'Name: ' + (d.name||''), 'Company: ' + (d.company||''),
    'Phone: ' + (d.phone||''), 'Country/Place: ' + (d.country||d.place||''),
    'Qty: ' + (d.qty||d.volume||''), 'Grades: ' + (d.grades||''),
    'Source: ' + (d.utm_source||d.src||d.ref||'direct') + (d.article ? ' / ' + d.article : ''), '',
    (d.message||'')].join('\n');
  MailApp.sendEmail(OWNER_EMAIL, '[' + s.priority + '] New lead ' + id + ' - ' + (d.company||d.name||''), body);
  if (d.email) {
    MailApp.sendEmail({to: d.email, replyTo: OWNER_EMAIL, name: 'Gujarat Bio Organics',
      subject: 'We received your enquiry - Gujarat Bio Organics',
      body: 'Hello ' + (d.name||'') + ',\n\nThank you for your enquiry (ref ' + id + '). Our team will reply within one working day with details.\n\n' +
        'If it is urgent, message us on WhatsApp: +91 99787 91167.\n\nGujarat Bio Organics Pvt. Ltd.\nBhavnagar, Gujarat, India\nhttps://www.gujaratbio.com'});
  }
}

function out(t) { return ContentService.createTextOutput(t); }

/* Run once from the editor to authorise mail + sheet access and add a test row */
function testLead() {
  doPost({postData:{contents: JSON.stringify({name:'Test Buyer',company:'Test Imports LLC',phone:'+968 0000 0000',
    email:OWNER_EMAIL,country:'Oman',qty:'1 container',form:'Export enquiry',channel:'wa',utm_source:'test'})}});
}

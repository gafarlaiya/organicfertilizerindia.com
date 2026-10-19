#!/usr/bin/env python3
"""Generates gbo-gtm-container.json, an importable Google Tag Manager web container for b2b.gujaratbio.com.
Import: GTM > Admin > Import Container > choose file > 'Merge' > 'Rename conflicting' (or Overwrite on a new empty container).
Edit the two Constant variables after import (GA4 Measurement ID is prefilled; Meta Pixel ID is a placeholder)."""
import json, re

GA4 = "G-HF0J0NF8G0"
PIXEL_PLACEHOLDER = "REPLACE_WITH_PIXEL_ID"
ALL_PAGES, INIT = "2147479553", "2147479573"

PARAMS = ["form_name", "lead_channel", "event_id", "link_location", "link_text", "grades_count", "video_id", "video_provider", "video_title", "page_type"]
base = {"accountId": "0", "containerId": "0", "fingerprint": "0"}

variables, n = [], 100
def var_const(name, value):
    global n; n += 1
    variables.append({**base, "variableId": str(n), "name": name, "type": "c", "parameter": [{"type": "TEMPLATE", "key": "value", "value": value}]})
def var_dl(key):
    global n; n += 1
    variables.append({**base, "variableId": str(n), "name": f"DLV - {key}", "type": "v", "parameter": [
        {"type": "INTEGER", "key": "dataLayerVersion", "value": "2"}, {"type": "BOOLEAN", "key": "setDefaultValue", "value": "false"},
        {"type": "TEMPLATE", "key": "name", "value": key}]})
var_const("Const - GA4 Measurement ID", GA4)
var_const("Const - Meta Pixel ID", PIXEL_PLACEHOLDER)
for k in PARAMS + ["traffic_type"]: var_dl(k)

triggers, t = [], 200
def trig(name, kind, value):
    global t; t += 1
    op = "EQUALS" if kind == "eq" else "MATCH_REGEX"
    triggers.append({**base, "triggerId": str(t), "name": name, "type": "CUSTOM_EVENT", "customEventFilter": [{"type": op, "parameter": [
        {"type": "TEMPLATE", "key": "arg0", "value": "{{_event}}"}, {"type": "TEMPLATE", "key": "arg1", "value": value}]}]})
    return str(t)
EVENTS = "generate_lead|click_whatsapp|click_phone|click_email|begin_quote|form_start|form_error|video_start|chat_open|chat_start|page_not_found"
T_EVENTS = trig("CE - GBO events (to GA4)", "re", f"^({EVENTS})$")
T_LEAD = trig("CE - generate_lead", "eq", "generate_lead")
T_CONTACT = trig("CE - click whatsapp/phone/email", "re", "^(click_whatsapp|click_phone|click_email)$")
T_CONSENT = trig("CE - cookie choice changed", "eq", "gbo_consent_update")

def table(rows):
    return {"type": "LIST", "list": [{"type": "MAP", "map": [{"type": "TEMPLATE", "key": "parameter", "value": a}, {"type": "TEMPLATE", "key": "parameterValue", "value": b}]} for a, b in rows]}
NEED_AD = {"consentStatus": "NEEDED", "consentType": {"type": "LIST", "listItem": [{"type": "TEMPLATE", "value": "ad_storage"}]}}
tags, g = [], 300
def tag(name, typ, params, trig_ids, consent=None):
    global g; g += 1
    tags.append({**base, "tagId": str(g), "name": name, "type": typ, "parameter": params, "firingTriggerId": trig_ids,
                 "tagFiringOption": "ONCE_PER_EVENT", "monitoringMetadata": {"type": "MAP"},
                 "consentSettings": consent or {"consentStatus": "NOT_SET"}})

tag("Google tag - GA4", "googtag", [
    {"type": "TEMPLATE", "key": "tagId", "value": "{{Const - GA4 Measurement ID}}"},
    {"type": "LIST", "key": "configSettingsTable", "list": table([("page_type", "{{DLV - page_type}}"), ("traffic_type", "{{DLV - traffic_type}}")])["list"]}], [INIT])
tag("GA4 - GBO events", "gaawe", [
    {"type": "BOOLEAN", "key": "sendEcommerceData", "value": "false"},
    {"type": "TEMPLATE", "key": "eventName", "value": "{{Event}}"},
    {"type": "TEMPLATE", "key": "measurementIdOverride", "value": "{{Const - GA4 Measurement ID}}"},
    {"type": "LIST", "key": "eventSettingsTable", "list": table([(k, "{{DLV - %s}}" % k) for k in PARAMS])["list"]}], [T_EVENTS])

PIX_BASE = ("<script>(function(){var pid='{{Const - Meta Pixel ID}}';if(window.fbq||pid.indexOf('REPLACE')>-1)return;"
            "!function(f,b,e,v,n,t,s){n=f.fbq=function(){n.callMethod?n.callMethod.apply(n,arguments):n.queue.push(arguments)};"
            "if(!f._fbq)f._fbq=n;n.push=n;n.loaded=!0;n.version='2.0';n.queue=[];t=b.createElement(e);t.async=!0;t.src=v;"
            "s=b.getElementsByTagName(e)[0];s.parentNode.insertBefore(t,s)}(window,document,'script','https://connect.facebook.net/en_US/fbevents.js');"
            "fbq('init',pid);fbq('track','PageView')})();</script>")
PIX_LEAD = ("<script>if(window.fbq){fbq('track','Lead',{content_name:'{{DLV - form_name}}',lead_channel:'{{DLV - lead_channel}}'},{eventID:'{{DLV - event_id}}'})}</script>")
PIX_CONTACT = ("<script>if(window.fbq){fbq('track','Contact',{content_name:'{{Event}}',link_location:'{{DLV - link_location}}'},{eventID:'{{DLV - event_id}}'})}</script>")
def html(s): return [{"type": "TEMPLATE", "key": "html", "value": s}, {"type": "BOOLEAN", "key": "supportDocumentWrite", "value": "false"}]
tag("Meta Pixel - base + PageView", "html", html(PIX_BASE), [ALL_PAGES, T_CONSENT], NEED_AD)
tag("Meta Pixel - Lead", "html", html(PIX_LEAD), [T_LEAD], NEED_AD)
tag("Meta Pixel - Contact", "html", html(PIX_CONTACT), [T_CONTACT], NEED_AD)

out = {"exportFormatVersion": 2, "exportTime": "2026-10-19 18:30:00", "containerVersion": {
    "path": "accounts/0/containers/0/versions/0", "accountId": "0", "containerId": "0", "containerVersionId": "0",
    "name": "GBO tracking v1 (GA4 events, consent-gated Meta Pixel)",
    "container": {"path": "accounts/0/containers/0", "accountId": "0", "containerId": "0", "name": "b2b.gujaratbio.com",
                  "publicId": "GTM-XXXXXXX", "usageContext": ["WEB"], "fingerprint": "0"},
    "tag": tags, "trigger": triggers, "variable": variables,
    "builtInVariable": [{"accountId": "0", "containerId": "0", "type": "EVENT", "name": "Event"}], "fingerprint": "0"}}
open("gbo-gtm-container.json", "w").write(json.dumps(out, indent=1))

# self-check: every {{ref}} resolves, every trigger id exists
names = {v["name"] for v in variables} | {"Event", "_event"}
tids = {tr["triggerId"] for tr in triggers} | {ALL_PAGES, INIT}
txt = json.dumps(out)
missing = {m for m in re.findall(r"\{\{([^}]+)\}\}", txt) if m not in names}
bad = [x for tg in tags for x in tg["firingTriggerId"] if x not in tids]
print("tags", len(tags), "triggers", len(triggers), "variables", len(variables), "| unresolved refs:", missing or "none", "| bad triggers:", bad or "none")

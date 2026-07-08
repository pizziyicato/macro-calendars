#!/usr/bin/env python3
"""Audit calendars/*.ics: structure, folding, unique UIDs, flags, weekday conventions."""
import os, re, sys, datetime as dt
MONFRI=set(range(5)); ANY=set(range(7))
W={"fed-":{2},"fedmin":{2},"ecb-":{3},"boe-":{3},"rba-":{1},"boc-":{2},"rbnz":{2},"snb-":{3},
   "copom":{2},"banxico":{3},"cbrt":{3},"bok-":{3,4},"bcrp":{3},"nbsrb":{3},"usnfp":{3,4},
   "mnb-":{1},"bi-":{2},"bnm-":{3},"bot-":{2},"bsp-":{3},"cbr-":{4},"nbu-":{3},"bcch":{1},
   "cnb-":{3},"nbp-":{2},"boi-":{0},"cbc-":{3},"cbi-":{2},"cbn-":{1},"cbk-":{1},"bog-":{0},
   "nbk-":{4},"cbe-":{3},"riks":{2,3},"sarb":{2,3},"norges":{3},"bnr-":{1,2},"bam-":{1},
   "usmid":{1},"uspres":{1},"sweden":{6},"latvia":{5},"zambia":{3},"jpcpi":{4}}
SHIFT1=("jpcpi","jptankan","jpgdp")
base=os.path.join(os.path.dirname(os.path.abspath(__file__)),"calendars")
uids,tot=set(),0
for fn in sorted(os.listdir(base)):
    if not fn.endswith(".ics") or fn.startswith("Feed-"): continue
    raw=open(os.path.join(base,fn),"rb").read().decode()
    assert raw.count("BEGIN:VEVENT")==raw.count("END:VEVENT"), fn
    assert all(len(l.encode())<=75 for l in raw.split("\r\n")), (fn,"fold>75")
    txt,cur=[],""
    for l in raw.split("\r\n"):
        if l.startswith(" "): cur+=l[1:]
        else:
            if cur: txt.append(cur)
            cur=l
    txt.append(cur)
    for e in "\n".join(txt).split("BEGIN:VEVENT")[1:]:
        uid=re.search(r"UID:([^\n@]+)",e).group(1)
        assert uid not in uids,("dup uid",uid); uids.add(uid)
        summ=re.search(r"SUMMARY:(.+)",e).group(1)
        assert any(0x1F1E6<=ord(c)<=0x1F1FF for c in summ) or "\U0001F310" in summ,(fn,"no flag",summ[:50])
        d=re.search(r"DTSTART(?:;VALUE=DATE)?:(\d{8})",e).group(1)
        if uid.startswith(SHIFT1): d=(dt.datetime.strptime(d,"%Y%m%d")+dt.timedelta(days=1)).strftime("%Y%m%d")
        if "RRULE:" not in e and not uid.startswith("rr-"):
            wd=dt.datetime.strptime(d,"%Y%m%d").weekday()
            for p,a in W.items():
                if uid.startswith(p): assert wd in a,(fn,uid,d,wd); break
        tot+=1
print(f"AUDIT PASS: {tot} events, {len(uids)} unique UIDs")

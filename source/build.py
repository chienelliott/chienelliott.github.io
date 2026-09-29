"""Lint + build the tutoring question set. Outputs quiz.html (artifact body),
handout.html (standalone, for PDF printing)."""
import base64, html, importlib, json, os, random, re, sys, statistics
_mod = importlib.import_module(sys.argv[1] if len(sys.argv) > 1 else "qset")
OUT = sys.argv[2] if len(sys.argv) > 2 else ""
QS, LECTURES = _mod.QS, _mod.LECTURES
TITLE = getattr(_mod, "TITLE", "Anatomy & Epithelium Practice")
SHORT = getattr(_mod, "SHORT", {"ANAT": "Anatomy", "EPI": "Epithelium"})

HERE = os.path.dirname(os.path.abspath(__file__))
IMG = os.path.join(HERE, "img")


def plain(t):
    return html.unescape(re.sub(r"<[^>]+>", "", t))


# ---------------- lint (mirrors build_questions.py rules) ----------------
errs, warns = [], []
ids = [q["id"] for q in QS]
assert len(ids) == len(set(ids)), "duplicate ids"
MP = re.compile(r"(,\s*and\s+(what|which|how|why|where|when)\b)"
                r"|(\band\s+(what|which|how|why|where|when)\s+"
                r"(is|are|was|were|does|do|did|kind|type|happens|follows|"
                r"component|organisms?|mechanism|principle|test|parameter|"
                r"curve|route|step|resource|other)\b)|(\?.*\?)", re.I)
PKG = re.compile(r"\s[-–]\s|;|→|,\s*(because|which is why|so |with )")
MATCH = re.compile(r"match (each|the|these|those)\b|pair (each|the)\b"
                   r"|which pairing|entirely correct|which set of"
                   r"|correct sequence|which combination|\brank (these|them)\b"
                   r"|arrange |\border (these|the)\b", re.I)
LETTER = re.compile(r"\b(option|answer|choice)\s+[A-F]\b|\([A-F]\)")
BRIT = re.compile(r"\b\w*(sulph|colour|haem|oedem|tumour|anaem|oesoph|"
                  r"fibre|centre|organis|recognis|minimis|categoris|"
                  r"characteris|visualis|specialis|ionis)\w*\b", re.I)
lt = 0
for q in QS:
    o = q["opts"]
    if not (2 <= len(o) <= 6) or not (0 <= q["ans"] < len(o)):
        errs.append(f"{q['id']}: option count/ans")
    if q["img"] and not os.path.exists(os.path.join(IMG, q["img"])):
        errs.append(f"{q['id']}: missing image {q['img']}")
    blob = " ".join([q["stem"], q["why"], q["flag"] or ""] + o)
    if "—" in blob or "&mdash;" in blob:
        errs.append(f"{q['id']}: em dash")
    for m in BRIT.finditer(blob):
        errs.append(f"{q['id']}: British spelling {m.group(0)!r}")
    if LETTER.search(q["why"]):
        errs.append(f"{q['id']}: explanation references an option letter")
    if q["origin"] == "prof":
        continue
    if MP.search(plain(q["stem"])):
        errs.append(f"{q['id']}: multi-part stem")
    pk = sum(1 for x in o if len([p for p in PKG.split(plain(x))
                                 if p and len(p.split()) >= 3]) >= 2)
    if pk >= len(o) * 0.6 or MATCH.search(plain(q["stem"])):
        errs.append(f"{q['id']}: compound options")
    if not all(len(plain(x).split()) <= 4 for x in o):
        L = [len(plain(x)) for x in o]
        k = L[q["ans"]]; mx = max(x for i, x in enumerate(L) if i != q["ans"])
        if k > 1.30 * mx:
            lt += 1
            errs.append(f"{q['id']}: length tell {k} vs {mx}")

# ---------------- shuffle (key authored first) ----------------
for q in QS:
    if q["origin"] == "prof" or q["ans"] != 0:
        continue            # lecturer's order kept
    rng = random.Random(getattr(_mod, "SALT", "tutor") + ":" + q["id"])
    idx = list(range(len(q["opts"])))
    rng.shuffle(idx)
    q["opts"] = [q["opts"][i] for i in idx]
    q["ans"] = idx.index(0)

pos = [q["ans"] for q in QS]
print(f"{len(QS)} questions  "
      + "  ".join(f"{k}={sum(1 for q in QS if q['lec']==k)}" for k in LECTURES))
print("answer positions:", {chr(65+i): pos.count(i) for i in range(6) if pos.count(i)})
print("image stems:", sum(1 for q in QS if q["img"]),
      " beyond:", sum(1 for q in QS if q["beyond"]),
      " flagged:", sum(1 for q in QS if q["flag"]),
      " origins:", {o: sum(1 for q in QS if q['origin']==o) for o in ("gen","prof","adapted","repaired")})
naming = [q for q in QS if all(len(plain(x).split()) <= 4 for x in q["opts"])]
prose = [q for q in QS if q not in naming and q["origin"] != "prof"]
longest = sum(1 for q in prose
              if len(plain(q["opts"][q["ans"]])) == max(len(plain(x)) for x in q["opts"]))
for q in prose:
    Lz = [len(plain(x)) for x in q["opts"]]
    if Lz[q["ans"]] == max(Lz):
        print(f"   longest key {q['id']}: {Lz[q['ans']]} vs next "
              f"{sorted(Lz)[-2]}")
print(f"prose questions: {len(prose)}; key is the longest option in {longest} "
      f"({100*longest/max(1,len(prose)):.0f}%, chance ~{100/statistics.mean(len(q['opts']) for q in prose):.0f}%)")
# coverage: option terms never used as a key (report only)
keys = {plain(q["opts"][q["ans"]]).lower() for q in QS}
dis = {}
for q in QS:
    if all(len(plain(x).split()) <= 4 for x in q["opts"]):
        for i, x in enumerate(q["opts"]):
            t = plain(x).lower()
            if i != q["ans"] and t not in keys:
                dis[t] = dis.get(t, 0) + 1
print("short distractors never a key:", ", ".join(sorted(dis)))
if errs:
    print("LINT FAILURES:\n  " + "\n  ".join(errs)); sys.exit(1)
print("lint ok")

# ---------------- emit ----------------
def data_uri(fn):
    with open(os.path.join(IMG, fn), "rb") as f:
        return "data:image/jpeg;base64," + base64.b64encode(f.read()).decode()

imgs = {q["img"]: data_uri(q["img"]) for q in QS if q["img"]}
payload = [{k: q[k] for k in ("id", "lec", "ref", "stem", "opts", "ans", "why",
                               "img", "beyond", "flag", "origin")} for q in QS]
tpl = open(os.path.join(HERE, "quiz_template.html"), encoding="utf-8").read()
out = (tpl.replace("/*__DATA__*/", json.dumps(payload, ensure_ascii=False))
          .replace("/*__IMGS__*/", json.dumps(imgs))
          .replace("/*__LECS__*/", json.dumps(LECTURES, ensure_ascii=False))
          .replace("/*__SHORT__*/", json.dumps(SHORT, ensure_ascii=False))
          .replace("__TITLE__", html.escape(TITLE)))
open(os.path.join(HERE, OUT + "quiz.html"), "w", encoding="utf-8").write(out)

# handout
L = []
A = "ABCDEF"
L.append(f"<!doctype html><html><head><meta charset='utf-8'><title>"
         f"{html.escape(TITLE)} – Handout</title><style>"
         "body{font:10.5pt/1.45 'Segoe UI',Arial,sans-serif;color:#1d1d1f;margin:0}"
         "h1{font-size:17pt;margin:0 0 2pt}h2{font-size:13pt;margin:16pt 0 6pt;"
         "border-bottom:1px solid #999;padding-bottom:3pt;break-after:avoid}"
         ".sub{color:#555;margin:0 0 10pt}.q{break-inside:avoid;margin:0 0 10pt}"
         ".q b.n{display:inline-block;min-width:2.6em}"
         ".q ol{margin:3pt 0 0 2.6em;padding:0;list-style:none}"
         ".q img{max-height:2.1in;max-width:3.6in;display:block;margin:4pt 0 4pt 2.6em;"
         "border:1px solid #ccc}"
         ".tag{font-size:8pt;color:#555;border:1px solid #aaa;border-radius:3px;"
         "padding:0 3pt;margin-left:4pt}"
         ".key{break-before:page}.k{break-inside:avoid;margin:0 0 7pt}"
         ".k .f{color:#6b5300;font-size:9.5pt}"
         "@page{margin:0.6in}</style></head><body>")
L.append(f"<h1>{html.escape(TITLE)}</h1><p class='sub'>"
         f"{len(QS)} questions. "
         + ("Items marked <span class='tag'>beyond the slides</span> need material "
            "the slides do not state. " if any(q["beyond"] for q in QS) else "")
         + "Answer key and explanations at the end.</p>")
n = 0
num = {}
for lec, name in LECTURES.items():
    L.append(f"<h2>{html.escape(name)}</h2>")
    for q in [x for x in QS if x["lec"] == lec]:
        n += 1; num[q["id"]] = n
        tag = "<span class='tag'>beyond the slides</span>" if q["beyond"] else ""
        im = f"<img src='{imgs[q['img']]}'>" if q["img"] else ""
        opts = "".join(f"<li>{A[i]}. {o}</li>" for i, o in enumerate(q["opts"]))
        L.append(f"<div class='q'><b class='n'>{n}.</b>{q['stem']}{tag}{im}<ol>{opts}</ol></div>")
L.append("<div class='key'><h1>Answer key</h1>")
for lec, name in LECTURES.items():
    L.append(f"<h2>{html.escape(name)}</h2>")
    for q in [x for x in QS if x["lec"] == lec]:
        f = (f"<div class='f'><b>Note:</b> {q['flag']}</div>" if q["flag"] else "")
        L.append(f"<div class='k'><b>{num[q['id']]}. {A[q['ans']]}</b> "
                 f"<i>({html.escape(q['ref'])})</i> – {q['why']}{f}</div>")
L.append("</div></body></html>")
open(os.path.join(HERE, OUT + "handout.html"), "w", encoding="utf-8").write("".join(L))
print(f"wrote {OUT}quiz.html, {OUT}handout.html")

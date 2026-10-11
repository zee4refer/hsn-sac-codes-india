"""Search the HSN / SAC lists by item name, Hindi/Hinglish word or code.  python3 search.py chawal"""
import json
import sys
from pathlib import Path

HERE = Path(__file__).parent


def search(q, limit=10):
    q = q.lower().strip()
    rows = json.loads((HERE / "hsn.json").read_text(encoding="utf-8"))
    rows += json.loads((HERE / "sac.json").read_text(encoding="utf-8"))
    def text(r):
        return " ".join(str(v) if not isinstance(v, list) else " ".join(v) for v in r.values()).lower()
    hits = [r for r in rows if q in text(r)]
    hits.sort(key=lambda r: (not str(r.get("code", "")).startswith(q), len(str(r.get("code", "")))))
    hits.sort(key=lambda r: (q not in r["search_words"].lower() and q not in r["common_items"].lower(), len(r["code"])))
    return hits[:limit]


if __name__ == "__main__":
    for r in search(" ".join(sys.argv[1:]) or "soap"):
        print(r["code"], "-", r["description"], "|", r["common_items"])

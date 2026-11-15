"""Check that the three course datasets match the recorded input manifest."""
from pathlib import Path
import hashlib
import json
import sys

root=Path(__file__).resolve().parents[1]/"data"
manifest=json.loads((root/"manifest.json").read_text())
failed=False
for entry in manifest["files"]:
    p=root/entry["path"]
    if not p.is_file():
        print("MISSING",entry["path"]);failed=True;continue
    digest=hashlib.sha256()
    with p.open("rb") as f:
        for chunk in iter(lambda:f.read(1024*1024),b""):digest.update(chunk)
    match=digest.hexdigest()==entry["sha256"]
    print("MATCH" if match else "DIFFERS",entry["path"])
    failed|=not match
sys.exit(1 if failed else 0)

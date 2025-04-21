#!/usr/bin/env python3
import os
import requests
from tqdm import tqdm

BASE_URL = "https://nvd.nist.gov/feeds/json/cve/1.1/"
DEST_DIR = "data/cve"

FILES = [
    "nvdcve-1.1-2024.json.gz",
    "nvdcve-1.1-2023.json.gz",
    "nvdcve-1.1-modified.json.gz",
    "nvdcve-1.1-recent.json.gz"
]

os.makedirs(DEST_DIR, exist_ok=True)

for filename in FILES:
    url = BASE_URL + filename
    dest_path = os.path.join(DEST_DIR, filename)
    print(f"Downloading {filename}...")
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(dest_path, 'wb') as f:
            for chunk in tqdm(r.iter_content(chunk_size=8192)):
                if chunk:
                    f.write(chunk)


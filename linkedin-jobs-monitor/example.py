"""Bounded example. Runs only when explicitly executed; requires your own APIFY_TOKEN."""
import json
import os
import urllib.request

RUN_INPUT = {'mode': 'preview', 'location': 'New York, United States', 'max_rows': 1, 'continuePreviousRun': False, 'max_pages': 1, 'searchTerms': 'software engineer'}
URL = 'https://api.apify.com/v2/acts/architekture~linkedin-jobs-monitor/run-sync-get-dataset-items?timeout=120&memory=2048&maxTotalChargeUsd=0.05'

def main():
    request = urllib.request.Request(URL, data=json.dumps(RUN_INPUT).encode(), method="POST", headers={"Content-Type":"application/json", "Authorization":"Bearer " + os.environ["APIFY_TOKEN"]})
    with urllib.request.urlopen(request, timeout=150) as response:
        rows = json.load(response)
    print(json.dumps(rows, indent=2, ensure_ascii=False))

if __name__ == "__main__":
    main()

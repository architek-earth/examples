"""Bounded example. Runs only when explicitly executed; requires your own APIFY_TOKEN."""
import json
import os
import urllib.request

RUN_INPUT = {'books': ['pinnacle'], 'includeBetfair': False, 'tours': ['ATP', 'WTA'], 'markets': ['match-winner'], 'hoursAhead': 24, 'maxMatchesPerBook': 1, 'maxItems': 2, 'incrementalMode': False, 'preview': True}
URL = 'https://api.apify.com/v2/acts/architekture~tennis-odds-scraper/run-sync-get-dataset-items?timeout=120&memory=2048&maxTotalChargeUsd=0.05'

def main():
    request = urllib.request.Request(URL, data=json.dumps(RUN_INPUT).encode(), method="POST", headers={"Content-Type":"application/json", "Authorization":"Bearer " + os.environ["APIFY_TOKEN"]})
    with urllib.request.urlopen(request, timeout=150) as response:
        rows = json.load(response)
    print(json.dumps(rows, indent=2, ensure_ascii=False))

if __name__ == "__main__":
    main()

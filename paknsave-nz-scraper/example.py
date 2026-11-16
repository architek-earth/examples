"""Bounded example. Runs only when explicitly executed; requires your own APIFY_TOKEN."""
import json
import os
import urllib.request

RUN_INPUT = {'continuePreviousRun': False, 'debugSaveResponses': False, 'includeDetails': False, 'maxItemsPerQuery': 1, 'maxRunSeconds': 60, 'operation': 'collect', 'preview': True, 'searchTerms': ['milk'], 'storeId': 'e1925ea7-01bc-4358-ae7c-c6502da5ab12'}
URL = 'https://api.apify.com/v2/acts/architekture~paknsave-nz-scraper/run-sync-get-dataset-items?timeout=120&memory=2048&maxTotalChargeUsd=0.1780000'

def main():
    request = urllib.request.Request(URL, data=json.dumps(RUN_INPUT).encode(), method="POST", headers={"Content-Type":"application/json", "Authorization":"Bearer " + os.environ["APIFY_TOKEN"]})
    with urllib.request.urlopen(request, timeout=150) as response:
        rows = json.load(response)
    print(json.dumps(rows, indent=2, ensure_ascii=False))

if __name__ == "__main__":
    main()

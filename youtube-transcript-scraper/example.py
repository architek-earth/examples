"""Bounded example. Runs only when explicitly executed; requires your own APIFY_TOKEN."""
import json
import os
import urllib.request

RUN_INPUT = {'fallbackToAnyLanguage': True, 'includeSegments': True, 'includeText': True, 'languages': ['en'], 'preferManualCaptions': True, 'preview': True, 'videos': ['https://www.youtube.com/watch?v=iG9CE55wbtY'], 'translateTo': '', 'maxConcurrency': 1}
URL = 'https://api.apify.com/v2/acts/architekture~youtube-transcript-scraper/run-sync-get-dataset-items?timeout=120&memory=2048&maxTotalChargeUsd=0.05'

def main():
    request = urllib.request.Request(URL, data=json.dumps(RUN_INPUT).encode(), method="POST", headers={"Content-Type":"application/json", "Authorization":"Bearer " + os.environ["APIFY_TOKEN"]})
    with urllib.request.urlopen(request, timeout=150) as response:
        rows = json.load(response)
    print(json.dumps(rows, indent=2, ensure_ascii=False))

if __name__ == "__main__":
    main()

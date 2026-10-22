# New World NZ Scraper

How to call [architekture/new-world-nz-scraper](https://apify.com/architekture/new-world-nz-scraper) with the example input from its listing and read the results.
For what it returns, the fields and pricing, see the [listing](https://apify.com/architekture/new-world-nz-scraper).

Every example needs an Apify API token in `APIFY_TOKEN` ([get one](https://console.apify.com/settings/integrations)).
Rows with `"recordType": "status"` are free and explain blocked, empty or invalid inputs.

## Python

```python
import os
from apify_client import ApifyClient  # pip install apify-client

client = ApifyClient(os.environ["APIFY_TOKEN"])
run_input = {
    "searchTerms": [
        "milk"
    ],
    "stores": [
        "New World Thorndon",
        "New World Queenstown"
    ],
    "maxItemsPerQuery": 20,
    "proxyConfiguration": {
        "useApifyProxy": True,
        "apifyProxyGroups": [
            "RESIDENTIAL"
        ],
        "apifyProxyCountry": "NZ"
    }
}

run = client.actor("architekture/new-world-nz-scraper").call(run_input=run_input)
for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    if item.get("recordType") == "status":  # free row explaining a blocked, empty or invalid input
        print("status:", item)
        continue
    print(item)
```

## Node.js

```js
// npm install apify-client
import { ApifyClient } from "apify-client";

const client = new ApifyClient({ token: process.env.APIFY_TOKEN });
const input = {
    "searchTerms": [
        "milk"
    ],
    "stores": [
        "New World Thorndon",
        "New World Queenstown"
    ],
    "maxItemsPerQuery": 20,
    "proxyConfiguration": {
        "useApifyProxy": true,
        "apifyProxyGroups": [
            "RESIDENTIAL"
        ],
        "apifyProxyCountry": "NZ"
    }
};

const run = await client.actor("architekture/new-world-nz-scraper").call(input);
const { items } = await client.dataset(run.defaultDatasetId).listItems();
for (const item of items) {
    if (item.recordType === "status") { console.log("status:", item); continue; } // free row
    console.log(item);
}
```

## curl

```bash
# Runs the actor, waits for it (up to 5 minutes) and returns the dataset items as JSON.
curl -sS -X POST "https://api.apify.com/v2/acts/architekture~new-world-nz-scraper/run-sync-get-dataset-items" \
  -H "Authorization: Bearer $APIFY_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
  "searchTerms": [
    "milk"
  ],
  "stores": [
    "New World Thorndon",
    "New World Queenstown"
  ],
  "maxItemsPerQuery": 20,
  "proxyConfiguration": {
    "useApifyProxy": true,
    "apifyProxyGroups": [
      "RESIDENTIAL"
    ],
    "apifyProxyCountry": "NZ"
  }
}'
```

## n8n

Import [n8n-workflow.json](n8n-workflow.json) (Workflows → Import from file), then on the **Run actor** node create a
Header Auth credential with name `Authorization` and value `Bearer <your token>`.
The node returns one n8n item per dataset row.

## Input used

```json
{
  "searchTerms": [
    "milk"
  ],
  "stores": [
    "New World Thorndon",
    "New World Queenstown"
  ],
  "maxItemsPerQuery": 20,
  "proxyConfiguration": {
    "useApifyProxy": true,
    "apifyProxyGroups": [
      "RESIDENTIAL"
    ],
    "apifyProxyCountry": "NZ"
  }
}
```

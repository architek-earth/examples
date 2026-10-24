# Google Hotels Scraper

How to call [architekture/google-hotels-scraper](https://apify.com/architekture/google-hotels-scraper) with the example input from its listing and read the results.
For what it returns, the fields and pricing, see the [listing](https://apify.com/architekture/google-hotels-scraper).

Every example needs an Apify API token in `APIFY_TOKEN` ([get one](https://console.apify.com/settings/integrations)).
Rows with `"recordType": "status"` are free and explain blocked, empty or invalid inputs.

## Python

```python
import os
from apify_client import ApifyClient  # pip install apify-client

client = ApifyClient(os.environ["APIFY_TOKEN"])
run_input = {
    "mode": "paid",
    "queries": [
        "London"
    ],
    "maxItemsPerQuery": 10
}

run = client.actor("architekture/google-hotels-scraper").call(run_input=run_input)
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
    "mode": "paid",
    "queries": [
        "London"
    ],
    "maxItemsPerQuery": 10
};

const run = await client.actor("architekture/google-hotels-scraper").call(input);
const { items } = await client.dataset(run.defaultDatasetId).listItems();
for (const item of items) {
    if (item.recordType === "status") { console.log("status:", item); continue; } // free row
    console.log(item);
}
```

## curl

```bash
# Runs the actor, waits for it (up to 5 minutes) and returns the dataset items as JSON.
curl -sS -X POST "https://api.apify.com/v2/acts/architekture~google-hotels-scraper/run-sync-get-dataset-items" \
  -H "Authorization: Bearer $APIFY_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
  "mode": "paid",
  "queries": [
    "London"
  ],
  "maxItemsPerQuery": 10
}'
```

## n8n

Import [n8n-workflow.json](n8n-workflow.json) (Workflows → Import from file), then on the **Run actor** node create a
Header Auth credential with name `Authorization` and value `Bearer <your token>`.
The node returns one n8n item per dataset row.

## Make

Create a custom variable `APIFY_TOKEN` with your token (Organization → Variables), then create a new scenario and
import [make-blueprint.json](make-blueprint.json) (⋯ → Import Blueprint). The **HTTP** module sends
`Authorization: Bearer {{var.organization.APIFY_TOKEN}}` and returns the dataset rows as one parsed array.
On a plan without custom variables, replace that header value with your token inside Make; never commit it.

## Input used

```json
{
  "mode": "paid",
  "queries": [
    "London"
  ],
  "maxItemsPerQuery": 10
}
```

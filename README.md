# architek.earth examples

Copy-paste code for calling every [architek.earth](https://github.com/architek-earth) actor on Apify: Python, Node.js, curl, an importable n8n workflow and an importable Make scenario blueprint.
Templates never contain a token: n8n reads it from a Header Auth credential, Make from the `APIFY_TOKEN` custom variable.
Each folder uses the example input from the actor's listing and reads the results from its dataset.

You need an Apify API token in `APIFY_TOKEN` ([get one](https://console.apify.com/settings/integrations)).
All actors are pay per result. Rows with `"recordType": "status"` are free; they explain blocked, empty or invalid inputs.

<!-- actors:start -->
| Actor | Templates | Apify |
|---|---|---|
| [Ad Intelligence Watchlist](ad-intelligence-watchlist/) | [n8n](ad-intelligence-watchlist/n8n-workflow.json) · [Make](ad-intelligence-watchlist/make-blueprint.json) | [listing](https://apify.com/architekture/ad-intelligence-watchlist) |
| [ALDI AU Scraper](aldi-au-product-scraper/) | [n8n](aldi-au-product-scraper/n8n-workflow.json) · [Make](aldi-au-product-scraper/make-blueprint.json) | [listing](https://apify.com/architekture/aldi-au-product-scraper) |
| [ALDI Ireland Scraper](aldi-ie-scraper/) | [n8n](aldi-ie-scraper/n8n-workflow.json) · [Make](aldi-ie-scraper/make-blueprint.json) | [listing](https://apify.com/architekture/aldi-ie-scraper) |
| [AliExpress Scraper](aliexpress-search-scraper/) | [n8n](aliexpress-search-scraper/n8n-workflow.json) · [Make](aliexpress-search-scraper/make-blueprint.json) | [listing](https://apify.com/architekture/aliexpress-search-scraper) |
| [Coles Scraper](coles-au-product-scraper/) | [n8n](coles-au-product-scraper/n8n-workflow.json) · [Make](coles-au-product-scraper/make-blueprint.json) | [listing](https://apify.com/architekture/coles-au-product-scraper) |
| [EU E-Invoice Parser](docparser-invoice-json/) | [n8n](docparser-invoice-json/n8n-workflow.json) · [Make](docparser-invoice-json/make-blueprint.json) | [listing](https://apify.com/architekture/docparser-invoice-json) |
| [Dunnes Stores Scraper](dunnes-ie-scraper/) | [n8n](dunnes-ie-scraper/n8n-workflow.json) · [Make](dunnes-ie-scraper/make-blueprint.json) | [listing](https://apify.com/architekture/dunnes-ie-scraper) |
| [Google Ads Transparency Scraper](google-ads-transparency-scraper/) | [n8n](google-ads-transparency-scraper/n8n-workflow.json) · [Make](google-ads-transparency-scraper/make-blueprint.json) | [listing](https://apify.com/architekture/google-ads-transparency-scraper) |
| [Google Hotels Scraper](google-hotels-scraper/) | [n8n](google-hotels-scraper/n8n-workflow.json) · [Make](google-hotels-scraper/make-blueprint.json) | [listing](https://apify.com/architekture/google-hotels-scraper) |
| [Google Jobs Scraper](google-jobs-scraper/) | [n8n](google-jobs-scraper/n8n-workflow.json) · [Make](google-jobs-scraper/make-blueprint.json) | [listing](https://apify.com/architekture/google-jobs-scraper) |
| [Google Shopping Scraper](google-shopping-scraper/) | [n8n](google-shopping-scraper/n8n-workflow.json) · [Make](google-shopping-scraper/make-blueprint.json) | [listing](https://apify.com/architekture/google-shopping-scraper) |
| [Google Trends Scraper](google-trends-scraper/) | [n8n](google-trends-scraper/n8n-workflow.json) · [Make](google-trends-scraper/make-blueprint.json) | [listing](https://apify.com/architekture/google-trends-scraper) |
| [Indeed Scraper](indeed-scraper/) | [n8n](indeed-scraper/n8n-workflow.json) · [Make](indeed-scraper/make-blueprint.json) | [listing](https://apify.com/architekture/indeed-scraper) |
| [LinkedIn Jobs Scraper](linkedin-jobs-monitor/) | [n8n](linkedin-jobs-monitor/n8n-workflow.json) · [Make](linkedin-jobs-monitor/make-blueprint.json) | [listing](https://apify.com/architekture/linkedin-jobs-monitor) |
| [Mercadona Scraper](mercadona-es-scraper/) | [n8n](mercadona-es-scraper/n8n-workflow.json) · [Make](mercadona-es-scraper/make-blueprint.json) | [listing](https://apify.com/architekture/mercadona-es-scraper) |
| [New World NZ Scraper](new-world-nz-scraper/) | [n8n](new-world-nz-scraper/n8n-workflow.json) · [Make](new-world-nz-scraper/make-blueprint.json) | [listing](https://apify.com/architekture/new-world-nz-scraper) |
| [Pak'nSave Scraper](paknsave-nz-scraper/) | [n8n](paknsave-nz-scraper/n8n-workflow.json) · [Make](paknsave-nz-scraper/make-blueprint.json) | [listing](https://apify.com/architekture/paknsave-nz-scraper) |
| [Sainsbury's Scraper](sainsburys-uk-scraper/) | [n8n](sainsburys-uk-scraper/n8n-workflow.json) · [Make](sainsburys-uk-scraper/make-blueprint.json) | [listing](https://apify.com/architekture/sainsburys-uk-scraper) |
| [Shopify Scraper](shopify-products-scraper/) | [n8n](shopify-products-scraper/n8n-workflow.json) · [Make](shopify-products-scraper/make-blueprint.json) | [listing](https://apify.com/architekture/shopify-products-scraper) |
| [Substack Scraper](substack-scraper/) | [n8n](substack-scraper/n8n-workflow.json) · [Make](substack-scraper/make-blueprint.json) | [listing](https://apify.com/architekture/substack-scraper) |
| [Tennis Scraper](tennis-data-scraper/) | [n8n](tennis-data-scraper/n8n-workflow.json) · [Make](tennis-data-scraper/make-blueprint.json) | [listing](https://apify.com/architekture/tennis-data-scraper) |
| [Tennis Odds Scraper](tennis-odds-scraper/) | [n8n](tennis-odds-scraper/n8n-workflow.json) · [Make](tennis-odds-scraper/make-blueprint.json) | [listing](https://apify.com/architekture/tennis-odds-scraper) |
| [Tesco UK Scraper](tesco-uk-scraper/) | [n8n](tesco-uk-scraper/n8n-workflow.json) · [Make](tesco-uk-scraper/make-blueprint.json) | [listing](https://apify.com/architekture/tesco-uk-scraper) |
| [Threads Replies Scraper](threads-replies-scraper/) | [n8n](threads-replies-scraper/n8n-workflow.json) · [Make](threads-replies-scraper/make-blueprint.json) | [listing](https://apify.com/architekture/threads-replies-scraper) |
| [TikTok Shop Scraper](tiktok-shop-products-scraper/) | [n8n](tiktok-shop-products-scraper/n8n-workflow.json) · [Make](tiktok-shop-products-scraper/make-blueprint.json) | [listing](https://apify.com/architekture/tiktok-shop-products-scraper) |
| [Unified Video Transcript API](unified-transcript-api/) | [n8n](unified-transcript-api/n8n-workflow.json) · [Make](unified-transcript-api/make-blueprint.json) | [listing](https://apify.com/architekture/unified-transcript-api) |
| [Woolworths AU Scraper](woolworths-au-product-scraper/) | [n8n](woolworths-au-product-scraper/n8n-workflow.json) · [Make](woolworths-au-product-scraper/make-blueprint.json) | [listing](https://apify.com/architekture/woolworths-au-product-scraper) |
| [Woolworths NZ Scraper](woolworths-nz-scraper/) | [n8n](woolworths-nz-scraper/n8n-workflow.json) · [Make](woolworths-nz-scraper/make-blueprint.json) | [listing](https://apify.com/architekture/woolworths-nz-scraper) |
| [Y Combinator Scraper](yc-companies-scraper/) | [n8n](yc-companies-scraper/n8n-workflow.json) · [Make](yc-companies-scraper/make-blueprint.json) | [listing](https://apify.com/architekture/yc-companies-scraper) |
| [Yelp Scraper](yelp-scraper/) | [n8n](yelp-scraper/n8n-workflow.json) · [Make](yelp-scraper/make-blueprint.json) | [listing](https://apify.com/architekture/yelp-scraper) |
| [YouTube Transcript Scraper](youtube-transcript-scraper/) | [n8n](youtube-transcript-scraper/n8n-workflow.json) · [Make](youtube-transcript-scraper/make-blueprint.json) | [listing](https://apify.com/architekture/youtube-transcript-scraper) |
<!-- actors:end -->

Folders are regenerated weekly from the public Apify listings.

## Help

Something wrong with an example or an actor? [Open an issue](https://github.com/architek-earth/examples/issues/new) or email [north@architek.earth](mailto:north@architek.earth).

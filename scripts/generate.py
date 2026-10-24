"""Regenerate one folder per live actor from the public Apify Store and each actor's public input schema.

Each folder shows how to call the actor with its listing's example input and read the dataset:
Python, Node, curl, an importable n8n workflow and an importable Make scenario blueprint.
No file ever contains a token: n8n reads it from a Header Auth credential, Make from a custom variable.
Usage: python scripts/generate.py
"""

import json
import pathlib
import re
import shutil
import urllib.request

API = "https://api.apify.com/v2"
USER = "architekture"
ROOT = pathlib.Path(__file__).resolve().parent.parent
START, END = "<!-- actors:start -->", "<!-- actors:end -->"


def get(path: str) -> dict:
    req = urllib.request.Request(f"{API}/{path}", headers={"Accept": "application/json"})
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.load(r)["data"]


def example_input(slug: str) -> dict:
    """The listing's prefilled input; required fields without a prefill use their default or a placeholder."""
    schema = get(f"acts/{USER}~{slug}/builds/default").get("inputSchema") or {}
    if isinstance(schema, str):
        schema = json.loads(schema)
    props = schema.get("properties") or {}
    required = set(schema.get("required") or [])
    out: dict = {}
    for key, p in props.items():
        if "prefill" in p:
            out[key] = p["prefill"]
        elif key in required:
            if "default" in p:
                out[key] = p["default"]
            elif p.get("enum"):
                out[key] = p["enum"][0]
            else:
                out[key] = f"YOUR_{re.sub(r'(?<!^)(?=[A-Z])', '_', key).upper()}"
    return out


def title(a: dict) -> str:
    return re.split(r"\s+[—–-]\s+", a["title"], maxsplit=1)[0].strip()


def py_literal(v: object, depth: int = 0) -> str:
    """JSON-style layout with Python literals (True/False/None)."""
    pad, inner = "    " * depth, "    " * (depth + 1)
    if isinstance(v, dict):
        if not v:
            return "{}"
        return "{\n" + ",\n".join(f"{inner}{json.dumps(k)}: {py_literal(x, depth + 1)}" for k, x in v.items()) + f"\n{pad}}}"
    if isinstance(v, list):
        if not v:
            return "[]"
        return "[\n" + ",\n".join(f"{inner}{py_literal(x, depth + 1)}" for x in v) + f"\n{pad}]"
    if v is None or isinstance(v, bool):
        return repr(v)
    return json.dumps(v, ensure_ascii=False)


def python_snippet(actor: str, inp: dict) -> str:
    body = py_literal(inp)
    return f'''import os
from apify_client import ApifyClient  # pip install apify-client

client = ApifyClient(os.environ["APIFY_TOKEN"])
run_input = {body}

run = client.actor("{actor}").call(run_input=run_input)
for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    if item.get("recordType") == "status":  # free row explaining a blocked, empty or invalid input
        print("status:", item)
        continue
    print(item)
'''


def node_snippet(actor: str, inp: dict) -> str:
    body = json.dumps(inp, indent=4, ensure_ascii=False)
    return f'''// npm install apify-client
import {{ ApifyClient }} from "apify-client";

const client = new ApifyClient({{ token: process.env.APIFY_TOKEN }});
const input = {body};

const run = await client.actor("{actor}").call(input);
const {{ items }} = await client.dataset(run.defaultDatasetId).listItems();
for (const item of items) {{
    if (item.recordType === "status") {{ console.log("status:", item); continue; }} // free row
    console.log(item);
}}
'''


def curl_snippet(actor: str, inp: dict) -> str:
    body = json.dumps(inp, indent=2, ensure_ascii=False).replace("'", "'\\''")
    return f'''# Runs the actor, waits for it (up to 5 minutes) and returns the dataset items as JSON.
curl -sS -X POST "https://api.apify.com/v2/acts/{actor.replace("/", "~")}/run-sync-get-dataset-items" \\
  -H "Authorization: Bearer $APIFY_TOKEN" \\
  -H "Content-Type: application/json" \\
  -d '{body}'
'''


def n8n_workflow(actor: str, name: str, inp: dict) -> dict:
    url = f"https://api.apify.com/v2/acts/{actor.replace('/', '~')}/run-sync-get-dataset-items"
    return {
        "name": f"{name} (Apify)",
        "nodes": [
            {"parameters": {}, "name": "Start", "type": "n8n-nodes-base.manualTrigger", "typeVersion": 1, "position": [0, 0],
             "id": "a1b2c3d4-0000-4000-8000-000000000001"},
            {"parameters": {
                "method": "POST", "url": url,
                "authentication": "genericCredentialType", "genericAuthType": "httpHeaderAuth",
                "sendBody": True, "specifyBody": "json", "jsonBody": json.dumps(inp, indent=2, ensure_ascii=False),
                "options": {"timeout": 300000},
            }, "name": "Run actor", "type": "n8n-nodes-base.httpRequest", "typeVersion": 4.2, "position": [240, 0],
             "id": "a1b2c3d4-0000-4000-8000-000000000002"},
        ],
        "connections": {"Start": {"main": [[{"node": "Run actor", "type": "main", "index": 0}]]}},
        "settings": {},
    }


def make_blueprint(actor: str, name: str, inp: dict) -> dict:
    """Make (make.com) scenario blueprint: one HTTP "Make a request" module; token from the APIFY_TOKEN custom variable."""
    url = f"https://api.apify.com/v2/acts/{actor.replace('/', '~')}/run-sync-get-dataset-items"
    return {
        "name": f"{name} (Apify)",
        "flow": [
            {
                "id": 1,
                "module": "http:ActionSendData",
                "version": 3,
                "parameters": {"handleErrors": True, "useNewZLibDeCompress": True},
                "mapper": {
                    "url": url,
                    "serializeUrl": False,
                    "method": "post",
                    "headers": [{"name": "Authorization", "value": "Bearer {{var.organization.APIFY_TOKEN}}"}],
                    "qs": [],
                    "bodyType": "raw",
                    "contentType": "application/json",
                    "data": json.dumps(inp, indent=2, ensure_ascii=False),
                    "parseResponse": True,
                    "timeout": "300",
                    "shareCookies": False,
                    "rejectUnauthorized": True,
                    "followRedirect": True,
                    "useQuerystring": False,
                    "gzip": True,
                    "useMtls": False,
                    "followAllRedirects": False,
                },
                "metadata": {"designer": {"x": 0, "y": 0}},
            }
        ],
        "metadata": {
            "instant": False,
            "version": 1,
            "scenario": {"roundtrips": 1, "maxErrors": 3, "autoCommit": True, "autoCommitTriggerLast": True,
                         "sequential": False, "confidential": False, "dataloss": False, "dlq": False,
                         "freshVariables": False},
            "designer": {"orphans": []},
        },
    }


TOKEN_RE = re.compile(r"apify_api_[A-Za-z0-9]{10,}|Bearer\s+(?!\{\{)[A-Za-z0-9_\-]{20,}")


def check_template(path: pathlib.Path) -> None:
    """Every template must parse as JSON and carry no token."""
    text = path.read_text(encoding="utf-8")
    json.loads(text)
    if TOKEN_RE.search(text):
        raise SystemExit(f"token-like string in {path}")


def readme(a: dict, actor: str, inp: dict) -> str:
    name = title(a)
    return f'''# {name}

How to call [{actor}](https://apify.com/{actor}) with the example input from its listing and read the results.
For what it returns, the fields and pricing, see the [listing](https://apify.com/{actor}).

Every example needs an Apify API token in `APIFY_TOKEN` ([get one](https://console.apify.com/settings/integrations)).
Rows with `"recordType": "status"` are free and explain blocked, empty or invalid inputs.

## Python

```python
{python_snippet(actor, inp).rstrip()}
```

## Node.js

```js
{node_snippet(actor, inp).rstrip()}
```

## curl

```bash
{curl_snippet(actor, inp).rstrip()}
```

## n8n

Import [n8n-workflow.json](n8n-workflow.json) (Workflows → Import from file), then on the **Run actor** node create a
Header Auth credential with name `Authorization` and value `Bearer <your token>`.
The node returns one n8n item per dataset row.

## Make

Create a custom variable `APIFY_TOKEN` with your token (Organization → Variables), then create a new scenario and
import [make-blueprint.json](make-blueprint.json) (⋯ → Import Blueprint). The **HTTP** module sends
`Authorization: Bearer {{{{var.organization.APIFY_TOKEN}}}}` and returns the dataset rows as one parsed array.
On a plan without custom variables, replace that header value with your token inside Make; never commit it.

## Input used

```json
{json.dumps(inp, indent=2, ensure_ascii=False)}
```
'''


def main() -> None:
    # Deprecated actors stay on Apify for existing users but get no examples folder.
    items = sorted((a for a in get(f"store?username={USER}&limit=200")["items"]
                    if not a.get("isDeprecated") and not get(f"acts/{USER}~{a['name']}").get("isDeprecated")),
                   key=lambda a: a["name"])
    live = set()
    rows = []
    for a in items:
        slug = a["name"]
        actor = f"{USER}/{slug}"
        inp = example_input(slug)
        folder = ROOT / slug
        folder.mkdir(exist_ok=True)
        (folder / "README.md").write_text(readme(a, actor, inp), encoding="utf-8", newline="\n")
        for fname, doc in (("n8n-workflow.json", n8n_workflow(actor, title(a), inp)),
                           ("make-blueprint.json", make_blueprint(actor, title(a), inp))):
            (folder / fname).write_text(json.dumps(doc, indent=2, ensure_ascii=False) + "\n", encoding="utf-8", newline="\n")
            check_template(folder / fname)
        live.add(slug)
        rows.append(f"| [{title(a)}]({slug}/) | [n8n]({slug}/n8n-workflow.json) · [Make]({slug}/make-blueprint.json) "
                    f"| [listing](https://apify.com/{actor}) |")
    # Folders for actors that left the store are removed.
    for d in ROOT.iterdir():
        if d.is_dir() and (d / "n8n-workflow.json").exists() and d.name not in live:
            shutil.rmtree(d)
    index = ROOT / "README.md"
    text = index.read_text(encoding="utf-8")
    head, rest = text.split(START, 1)
    _, tail = rest.split(END, 1)
    table = "\n".join(["| Actor | Templates | Apify |", "|---|---|---|", *rows])
    index.write_text(f"{head}{START}\n{table}\n{END}{tail}", encoding="utf-8", newline="\n")
    print(f"{len(live)} actors, {2 * len(live)} templates (n8n + Make)")


if __name__ == "__main__":
    main()

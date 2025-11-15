import json
import requests

url = "https://api.senkuro.me/graphql"

headers = {
    "Content-Type": "application/json",
    "User-Agent": "Mozilla/5.0"
}

payload = {
    "operationName": "fetchMangaChapter",
    "variables": {
        "cdnQuality": "auto",
        "slug": "190051380671563298"
    },
    "extensions": {
        "persistedQuery": {
            "version": 1,
            "sha256Hash": "320a2637126c71ccdbce6af04325fe2f5878cc7adf9e90d06bdd6752f9bbb14e"
        }
    }
}

response = requests.post(url, json=payload, headers=headers)

data = response.json()
print(json.dumps(data, indent=4, ensure_ascii=False))


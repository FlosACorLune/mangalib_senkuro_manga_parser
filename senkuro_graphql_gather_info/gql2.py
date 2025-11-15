import aiohttp
import asyncio
import json

async def fetch_manga(slug: str):
    url = "https://api.senkuro.me/graphql"

    headers = {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0"
    }

    payload = {
        "operationName": "fetchManga",
        "variables": {
            "slug": slug
        },
        "extensions": {
            "persistedQuery": {
                "version": 1,
                "sha256Hash": "6d8b28abb9a9ee3199f6553d8f0a61c005da8f5c56a88ebcf3778eff28d45bd5"
            }
        }
    }

    async with aiohttp.ClientSession() as session:
        async with session.post(url, json=payload, headers=headers) as response:
            data = await response.json()
            print(json.dumps(data, indent=2, ensure_ascii=False))
            return data

# Запуск
if __name__ == "__main__":
    data = asyncio.run(fetch_manga("when-a-genius-office-worker-crosses-the-line"))
    print(data['data']['manga']['slug'])


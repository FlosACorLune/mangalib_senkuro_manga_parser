import aiohttp
import asyncio
import json

async def fetch_chapters(branch_id: str, after: str = None):
    url = "https://api.senkuro.me/graphql"
    headers = {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0"
    }
    payload = {
        "operationName": "fetchMangaChapters",
        "variables": {
            "after": after,
            "branchId": branch_id,
            "number": None,
            "orderBy": {
                "direction": "DESC",
                "field": "NUMBER"
            }
        },
        "extensions": {
            "persistedQuery": {
                "version": 1,
                "sha256Hash": "8c854e121f05aa93b0c37889e732410df9ea207b4186c965c845a8d970bdcc12"
            }
        }
    }

    async with aiohttp.ClientSession() as session:
        async with session.post(url, json=payload, headers=headers) as response:
            return await response.json()

# Пример запуска
if __name__ == "__main__":
    data = asyncio.run(fetch_chapters("TUFOR0FfQlJBTkNIOjUxNTc0NDQzMTU5NDEzMTYz"))
    #print(json.dumps(data, indent=4, ensure_ascii=False))
    print(data)
    for i in range(0,100):
        print(data['data']['mangaChapters']['edges'][i]['node']['slug'])
        print(data['data']['mangaChapters']['edges'][i]['node']['number'])
        print(data['data']['mangaChapters']['edges'][i]['node']['volume'])
        print(data['data']['mangaChapters']['edges'][i]['node']['createdAt'])
        print("--------------------------")

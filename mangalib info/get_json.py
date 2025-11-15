import json, requests

parameters = "?fields[]=background&fields[]=eng_name&fields[]=otherNames&fields[]=summary&fields[]=releaseDate&fields[]=type_id&fields[]=caution&fields[]=views&fields[]=close_view&fields[]=rate_avg&fields[]=rate&fields[]=genres&fields[]=tags&fields[]=teams&fields[]=user&fields[]=franchise&fields[]=authors&fields[]=publisher&fields[]=userRating&fields[]=moderated&fields[]=metadata&fields[]=metadata.count&fields[]=metadata.close_comments&fields[]=manga_status_id&fields[]=chap_count&fields[]=status_id&fields[]=artists&fields[]=format"
api_url = "https://api.cdnlibs.org/api/manga/"
server_one = "https://img2.imglib.info"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36 Edg/140.0.0.0",
    "Accept": "*/*",
    "Accept-Language": "en-US,en;q=0.9",
    "Content-Type": "application/json",
    "Origin": "https://mangalib.org",
    "Referer": "https://mangalib.org/",
    "Site-Id": "1",
    "Client-Time-Zone": "Asia/Yekaterinburg",
}

def get_json(url):
    response = requests.get(url, headers=HEADERS)
    return response.json()
slug = "208090--chihaya-restart"


query_chapters = f'{api_url}{slug}/chapters'
query_fields = f'{api_url}{slug}{parameters}'

result_query_fields = get_json(query_fields)
result_query_chapters = get_json(query_chapters)

with open("out.json", "w", encoding="utf-8") as f:
    json.dump(result_query_chapters, f, ensure_ascii=False, indent=4)

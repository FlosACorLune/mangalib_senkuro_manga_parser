## Коротко
Файл в основном содержит информацию которая есть на фронте. Reviews, Кол просмотров, Жанры и тд. Можете посмотреть в payload. 
В short - все нужное
В full - все fields что есть отправляется дефолтно

### orig network requests
https://api.cdnlibs.org/api/manga/208090--chihaya-restart?fields[]=background&fields[]=eng_name&fields[]=otherNames&fields[]=summary&fields[]=releaseDate&fields[]=type_id&fields[]=caution&fields[]=views&fields[]=close_view&fields[]=rate_avg&fields[]=rate&fields[]=genres&fields[]=tags&fields[]=teams&fields[]=user&fields[]=franchise&fields[]=authors&fields[]=publisher&fields[]=userRating&fields[]=moderated&fields[]=metadata&fields[]=metadata.count&fields[]=metadata.close_comments&fields[]=manga_status_id&fields[]=chap_count&fields[]=status_id&fields[]=artists&fields[]=format

## API
https://api.cdnlibs.org/api/manga/

## payload 
    fields[]=background&fields[]=eng_name&fields[]=otherNames&fields[]=summary&fields[]=releaseDate&fields[]=type_id&fields[]=caution&fields[]=views&fields[]=close_view&fields[]=rate_avg&fields[]=rate&fields[]=genres&fields[]=tags&fields[]=teams&fields[]=user&fields[]=franchise&fields[]=authors&fields[]=publisher&fields[]=userRating&fields[]=moderated&fields[]=metadata&fields[]=metadata.count&fields[]=metadata.close_comments&fields[]=manga_status_id&fields[]=chap_count&fields[]=status_id&fields[]=artists&fields[]=format

## Headers
    "Referer": "https://mangalib.org/", --нужен поскольку тут реализована hotlink защита(в chapters такого не нужно). То есть нельзя просто напрямую сделать запрос по url 
    "Site-Id": "1",


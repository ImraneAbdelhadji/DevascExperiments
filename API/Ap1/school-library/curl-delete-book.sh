APIKEY=$(bash curl-dynamic-apikey.sh | tail -n 1)

BOOK=$1

curl -X DELETE "http://library.demo.local/api/v1/books/$BOOK" \
-H "accept: application/json" \
-H "X-API-Key: $APIKEY"

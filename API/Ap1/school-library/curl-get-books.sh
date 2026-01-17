APIKEY=$(bash curl-dynamic-apikey.sh | tail -n 1)

curl -X GET "http://library.demo.local/api/v1/books" \
-H "accept: application/json" \
-H "X-API-Key: $APIKEY"

APIKEY=$(bash curl-dynamic-apikey.sh | tail -n 1)

curl -X POST "http://library.demo.local/api/v1/books" \
-H "accept: application/json" \
-H "Content-Type: application/json" \
-H "X-API-Key: $APIKEY" \
-d '{
    "id": 0,
    "title": "New DevOps Book",
    "author": "Student",
    "pages": 200
}'

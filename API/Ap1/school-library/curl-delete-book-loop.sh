APIKEY=$(bash curl-dynamic-apikey.sh | tail -n 1)

for (( book=900; book<=910; book++ ))
do
    echo "Deleting book $book"
    curl -X DELETE "http://library.demo.local/api/v1/books/$book" \
    -H "accept: application/json" \
    -H "X-API-Key: $APIKEY"
done
#!/bin/bash

loc1="London"
loc2="Brussels"


API_KEY="765c26843c0ca5230864251a31dcbdb7"

echo "Weer voor ($loc1)"
curl -G "https://api.openweathermap.org/data/2.5/weather" \
  --data-urlencode "q=$loc1" \
  --data-urlencode "appid=$API_KEY" \
  --data-urlencode "units=metric"

echo "--------------------------------"
echo "Weer voor ($loc2)"
curl -G "https://api.openweathermap.org/data/2.5/weather" \
  --data-urlencode "q=$loc2" \
  --data-urlencode "appid=$API_KEY" \
  --data-urlencode "units=metric"
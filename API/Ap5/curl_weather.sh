#!/bin/bash

API_KEY="765c26843c0ca5230864251a31dcbdb7"

echo "Weer voor London"
curl "https://api.openweathermap.org/data/2.5/weather?q=London&appid=$API_KEY&units=metric"

echo
echo "Weer voor Brussels"
curl "https://api.openweathermap.org/data/2.5/weather?q=Brussels&appid=$API_KEY&units=metric"

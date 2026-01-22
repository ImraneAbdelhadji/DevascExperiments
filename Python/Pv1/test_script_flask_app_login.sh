# test script for flask_app_login.py -- use in Virtualbox VM, not in Docker
# programm flask_app_login needs to be running
echo "Deleting all test records"
curl -k -X DELETE "https://127.0.0.1:5555/delete/all"
USER1="Imrane"
PW1="123"
USER2="Abdel"
PW2="123"

echo "Creating user 1"
curl -X POST -F "username=$USER1" -F "password=$PW1" http://127.0.0.1:5555/signup

echo
echo "Logging in user 1"
curl -X POST -F "username=$USER1" -F "password=$PW1" http://127.0.0.1:5555/login

echo
echo "Creating user 2"
curl -X POST -F "username=$USER2" -F "password=$PW2" http://127.0.0.1:5555/signup

echo
echo "Logging in user 2"
curl -X POST -F "username=$USER2" -F "password=$PW2" http://127.0.0.1:5555/login
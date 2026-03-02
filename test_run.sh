#!/usr/bin/env zsh

# If you'd want to automate your workflow
# you can use this script I made 
# It uses koko, a lightweight http tool like curl
# but is paired with jq, bat and other pages for
# handling different kinds of responses from server
# You can check it out at https://github.com/persona-mp3/koko.git
# And then you can follow the instructions for installing it
# If you'd want more features or anything to update let me know
flask --app main run & 
flask_id=$!

sleep 1

echo "\n Making normal get request to :5000/artists"
koko -ep http://localhost:5000/artists

echo "\n Making post via url params"

koko -post -ep "http://localhost:5000/artists?name=mass+of+the+fermenting+dreggs&genre=japanese-rock"

echo "\n Making post without url params"
koko -post -ep "http://localhost:5000/artists?"

kill $flask_id

echo 
echo " Killed flask process: $flask_id. Clean up done!"


#!/usr/bin/env zsh


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


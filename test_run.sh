#!/usr/bin/env zsh

flask --app main run & 
flask_id=$!

sleep 1

echo "running normal get"
koko -ep http://localhost:5000/artists

echo "\nrunning post"

# koko -post -ep http://localhost:5000/artists?name="mass of the fermenting dreggs"?genre="japanese-rock"
koko -post -ep "http://localhost:5000/artists?name=mass+of+the+fermenting+dreggs&genre=japanese-rock"

echo "None\n"
koko -post -ep "http://localhost:5000/artists?"

kill $flask_id

echo "Killed flask process: $flask_id"

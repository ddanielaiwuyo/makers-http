import json
import random

from flask import Flask, Request, Response, request, jsonify
app = Flask(__name__)

class Artist:
    def __init__(self, name, genre) -> None:
        self.name = name
        self.genre = genre

    def to_json(self) -> str:
        return json.dumps(self, default=lambda o: o.__dict__)
    
    def to_dict(self):
        return {
                "name": self.name,
                "genre": self.genre
        }

sugarhill = Artist("SugarHill", "uk-rap")
bill = Artist("Bill Evans", "Jazz")
spice = Artist("Ice-Spice", "Gra-Gra")

all_artists =  [sugarhill, bill, spice ]

def gen_artist() -> Artist:
    sugarhill = Artist("SugarHill", "uk-rap")
    bill = Artist("Bill Evans", "Jazz")
    spice = Artist("Ice-Spice", "Gra-Gra")

    artists = [ sugarhill, bill ,spice ]

    random.choice(artists)


@app.route("/artists", methods=["GET", "POST"])
def aritst() -> None:
    if request.method == "POST":
        print("handling post request from client")
        return "still under construction"

    artist_json = [artist.__dict__ for artist in all_artists]
    
    res_body = jsonify(artist_json)
    print("sent response")
    return res_body

    


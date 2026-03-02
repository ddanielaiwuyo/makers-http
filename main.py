from dataclasses import asdict
from flask import Flask, Request, Response, jsonify, request
from entities.Artist import Artist, get_all_artists

app = Flask(__name__)

MAX_PAYLOAD = 1500

def handle_post_request(req: Request) -> Response:
    print("handling post request")

    if req.content_length and req.content_length >= MAX_PAYLOAD:
        response = jsonify({"status_code": 418, "status": "I am a teapot"})
        return response

    artist_name = req.args.get("name")
    genre = req.args.get("genre")
    
    if artist_name is None or genre is None:
        response = jsonify({"status_code": 400, "status": "Bad request"})
        return response

    print("query params extracted")
    print(artist_name, genre)
    response = jsonify({"status_code": 201, "status": "OK"})
    return response

@app.route("/artists", methods=["GET", "POST"])
def handle_artists():
    if request.method == "POST":
        return handle_post_request(request)

    all_artists = get_all_artists(4)
    res_body = [asdict(artist) for artist in all_artists]
    return jsonify(res_body)


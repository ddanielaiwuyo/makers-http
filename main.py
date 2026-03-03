from dataclasses import asdict
from flask import Flask, Request, Response, jsonify, request
# from entities.artist import Artist
from entities.artist import Artist
from lib.artist_repository import ArtistRepository
from lib.database_connection import DatabaseConnection

app = Flask(__name__)

MAX_PAYLOAD = 1500

DB_CONN = DatabaseConnection()
DB_CONN.connect()
DB_CONN.seed()

artist_repo = ArtistRepository(DB_CONN)


@app.route("/artists", methods=["GET"])
def get_artists():
    db_response = artist_repo.get_all()
    db_response = [asdict(artist) for artist in db_response]
    return jsonify(db_response)

@app.route("/artists", methods=["POST"])
def create_artist():
    if request.content_length and request.content_length >= MAX_PAYLOAD:
        response = jsonify({"status_code": 418, "status": "I am a teapot"})
        return response

    artist_name = request.args.get("name")
    genre = request.args.get("genre")
    
    if artist_name is None or genre is None:
        response = jsonify({"status_code": 400, "status": "Bad request"})
        return response

    artist = Artist(None, artist_name, genre)
    artist_repo.create(artist)
    response = jsonify({"status_code": 201, "status": "OK"})
    response.status_code = 201
    return response

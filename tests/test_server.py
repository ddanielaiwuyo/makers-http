"""
GET /artists
"""

from dataclasses import asdict
from datetime import datetime
from flask import jsonify
from pytest import fixture
from entities.artist import Artist, Album


@fixture
def expected_res():
    artist_1 = Artist(1, "Pixies", "Rock")
    artist_1.albums = [Album(1, "Doolittle", "1983-01-01")]

    artist_2 = Artist(2, "The Beatles", "Alternative")
    artist_2.albums = [Album(2, "Abbey Road", "1969-01-01")]

    artist_3 = Artist(3, "Bill Evans", "Jazz")
    artist_3.albums = [Album(3, "Dig Bill Evans", "2021-05-01")]

    artist_4 = Artist(4, "Phantogram", "Niche")
    artist_4.albums = [Album(4, "Eyelid Movies", "2010-01-01")]

    res = [artist_1, artist_2, artist_3, artist_4]
    res = [asdict(artist) for artist in res]
    print("as dict-res", res)
    return res


def test_get_artists(web_client, expected_res, db_conn):
    db_conn.seed()
    res = web_client.get("/artists")
    print("response from server", res)

    assert res.status_code == 200
    assert res.get_json() == expected_res


def test_post_artist(web_client, db_conn):
    db_conn.seed()
    response = web_client.post(
        "/artists",
        query_string={"name": "Mass of the fermenting dreggs", "genre": "Rock"},
    )
    
    assert response.status_code == 201

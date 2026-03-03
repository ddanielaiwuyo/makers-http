from datetime import date
from entities.artist import Artist, Album
from pytest import fixture
from lib.artist_repository import ArtistRepository

@fixture
def expected_result():
    artist_1 = Artist(1, "Pixies", "Rock")
    artist_1.albums = [Album(1, "Doolittle", "1983-01-01")]

    artist_2 = Artist(2, "The Beatles", "Alternative")
    artist_2.albums = [Album(2, "Abbey Road", "1969-01-01")]

    artist_3 = Artist(3, "Bill Evans", "Jazz")
    artist_3.albums = [Album(3, "Dig Bill Evans", "2021-05-01")]

    artist_4 = Artist(4, "Phantogram", "Niche")
    artist_4.albums = [Album(4, "Eyelid Movies", "2010-01-01")]

    res = [artist_1, artist_2, artist_3, artist_4]
    return res

def test_artist_repostiory_all(db_conn, expected_result):
    db_conn.seed("seeds/http_challenge_1.sql")

    artist_repo = ArtistRepository(db_conn)
    actual_result = artist_repo.get_all()


    assert actual_result == expected_result

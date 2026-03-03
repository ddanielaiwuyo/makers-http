from datetime import date
from lib.database_connection import DatabaseConnection
from lib.album_repository import AlbumRepository
from entities.album import Album

def test_album_repostiory_all():
    conn = DatabaseConnection()
    conn.connect()
    conn.seed()


    album_repo = AlbumRepository(conn)
    actual_result = album_repo.all()

    expected_result =  [
        Album(1, "Doolittle", date.fromisoformat("1983-01-01"), 1),
        Album(2, 'Abbey Road', date.fromisoformat('1969-01-01'), 2),
        Album(3, 'Dig Bill Evans', date.fromisoformat('2021-05-01'), 3),
        Album(4, 'Eyelid Movies', date.fromisoformat('2010-01-01'), 4),
    ]

    assert actual_result == expected_result

from entities.album import Album

class AlbumRepository:
    def __init__(self, conn):
        self._conn = conn

    def all(self):
        query = "SELECT * FROM albums"
        response = self._conn.execute(query)
        if response is None:
            return response

        albums = []
        for row in response:
            album = Album(row["album_id"], row["title"], row["release_year"], row["artist_id"])
            albums.append(album)

        return albums

    def find(self, id):
        query = "SELECT * FROM albums WHERE album_id = %s"
        params = [id]

        response = self._conn.execute(query, params)
        if response is None:
            return response

        print("response for id", id)
        print(response)
        albums = []
        for row in response:
            album = Album(row["album_id"], row["title"], row["release_year"], row["artist_id"])
            albums.append(album)

        return albums

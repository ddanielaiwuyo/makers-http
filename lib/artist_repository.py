from datetime import datetime
from entities.Artist import Artist, Album

class ArtistRepository:
    def __init__(self, db_conn):
        self.conn = db_conn

    def get_all(self) -> list[Artist]:
        query = """
        select * from artists
        left join albums
        on albums.artist_id = artists.artist_id
        """
        response = self.conn.execute(query)
        all_artists = []
        for row in response:
            artist = Artist(row["artist_id"], row["name"], row["genre"])
            album = Album(row["album_id"],row["title"], row["release_year"].isoformat())
            artist.albums = [album]
            all_artists.append(artist)

        return all_artists

    def create(self, artist: Artist):
        query = """
        INSERT INTO artists (name, genre)
        VALUES(%s, %s);
        """


        params = [artist.name, artist.genre]

        self.conn.execute(query, params)

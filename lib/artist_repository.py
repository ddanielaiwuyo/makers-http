from datetime import datetime
from entities.artist import Artist, Album

class ArtistRepository:
    def __init__(self, db_conn):
        self.conn = db_conn

    def get_all(self) -> list[Artist]:
        # to avoid double column  names
        query = """
        select  
            artists.artist_id AS artist_id,
            artists.name AS name,
            artists.genre,
            albums.album_id,
            albums.title,
            albums.release_year 
        from artists
        left join albums
        on artists.artist_id = albums.artist_id
        """
        response = self.conn.execute(query)
        all_artists = []
        for row in response:
            artist = Artist(row["artist_id"], row["name"], row["genre"])
            release_year = row["release_year"].isoformat() if row["release_year"] is not None else None
            album = Album(row["album_id"],row["title"], release_year, row["artist_id"])
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

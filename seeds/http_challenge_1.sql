-- CREATE DATABASE http-challenge-1; 

DROP TABLE IF EXISTS albums;
DROP TABLE IF EXISTS artists;

CREATE TABLE IF NOT EXISTS artists (
	artist_id SERIAL PRIMARY KEY NOT NULL,
	name VARCHAR(200) NOT NULL,
	genre VARCHAR(200) NOT NULL,
	created_at TIMESTAMP DEFAULT LOCALTIMESTAMP
);

CREATE TABLE IF NOT EXISTS albums (
	album_id SERIAL PRIMARY KEY NOT NULL,
	title VARCHAR(200) NOT NULL,
	release_year DATE NOT NULL,
	artist_id INT REFERENCES artists(artist_id),
	created_at TIMESTAMP DEFAULT LOCALTIMESTAMP
);


INSERT INTO artists(name, genre) 
VALUES ('Pixies', 'Rock'), 
('The Beatles', 'Alternative'),
('Bill Evans', 'Jazz'),
('Phantogram', 'Niche');


INSERT INTO albums(title, release_year, artist_id)
VALUES ('Doolittle', '1983-01-01', 1),
('Abbey Road', '1969-01-01', 2),
('Dig Bill Evans', '2021-05-01', 3),
('Eyelid Movies', '2010-01-01', 4);



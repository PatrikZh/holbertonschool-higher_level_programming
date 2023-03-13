-- Lisiting all genres from hbtn_0d_tvshows and displays the number of shows linked to each
SELECT tv_genres.name AS genre, COUNT(tv_shows_genres.genre.id) AS number_of_shows FROM tv_genres LEFT JOIN tv_shows_genres ON tv_genres.id = tv_shows_genres.genre_id GROUP BY tv_genres.genre.id ORDER BY number_of_shows DESC;

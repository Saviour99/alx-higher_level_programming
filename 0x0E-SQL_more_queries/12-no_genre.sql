-- A script that lists all shows contained in hbtn_0d_tvshows without a genre linked.

SELECT tv_shows.title, NULL AS genre_id FROM tv_show WHERE tv_show_id IS NULL ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC

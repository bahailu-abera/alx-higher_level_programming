-- Lists all shows contained in hbtn_0d_tvshows
-- that have at least one genre linked.
SELECT ts.title, tg.genre_id
FROM tv_shows ts INNER JOIN tv_show_genres tg
ON ts.id = tg.show_id;

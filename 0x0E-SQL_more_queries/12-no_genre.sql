-- List all shows without genre link
-- Query To list all shows without genre link
SELECT ts.title, tg.genre_id
FROM tv_shows ts LEFT JOIN tv_show_genres tg
ON ts.id = tg.show_id WHERE tg.genre_id IS NULL
ORDER BY ts.title, tg.genre_id;

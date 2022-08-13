-- List all genres not linked to the show Dexter
-- Query to list all genres not linked to the show Dexter
SELECT tg.name
FROM tv_genres tg LEFT JOIN (SELECT tg.id, tg.name
     FROM tv_genres tg LEFT JOIN tv_show_genres tsg
     ON tg.id = tsg.genre_id
     LEFT JOIN tv_shows ts
     ON ts.id = tsg.show_id
     WHERE ts.title = "Dexter")
     AS t
ON tg.id = t.id
WHERE t.id IS NULL
ORDER BY tg.name;

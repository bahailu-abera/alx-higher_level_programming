SELECT ts.title
FROM tv_shows ts LEFT JOIN (SELECT ts.id, ts.title
     FROM tv_shows ts INNER JOIN tv_show_genres tsg
     ON ts.id = tsg.show_id
     LEFT JOIN tv_genres tg
     ON tg.id = tsg.genre_id
     WHERE tg.name = "Comedy"
     ) AS temp
ON ts.id = temp.id
WHERE temp.id IS NULL
ORDER BY ts.title;

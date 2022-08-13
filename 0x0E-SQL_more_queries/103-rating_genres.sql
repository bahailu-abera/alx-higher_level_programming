-- Lists all genres by rating
-- Query to list all genres by rating
SELECT tg.name, SUM(tsr.rate) AS rating
FROM tv_show_genres tsg LEFT JOIN tv_show_ratings tsr
ON tsg.show_id = tsr.show_id LEFT JOIN tv_genres tg
ON tg.id = tsg.genre_id
GROUP BY tg.name
ORDER BY rating DESC;

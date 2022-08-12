-- Count list of all genres with shows
-- Query to count and display all shows of genres
SELECT tg.name as genre, COUNT(tg.name) AS number_of_shows
FROM tv_genres tg INNER JOIN tv_show_genres tsg
ON tg.id = tsg.genre_id
GROUP BY tg.name
ORDER BY number_of_shows DESC;

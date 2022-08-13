-- List all shows by their rating
-- Query to list all shows by their rating
SELECT ts.title, SUM(tsr.rate) AS rating
FROM tv_shows ts LEFT JOIN tv_show_ratings tsr
ON ts.id = tsr.show_id
GROUP BY ts.title
ORDER BY rating DESC;

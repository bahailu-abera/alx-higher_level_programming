-- Max value
-- Query to display max value
SELECT state, MAX(value) AS max_temp
FROM temperatures
GROUP BY state
ORDER BY state
LIMIT 3;

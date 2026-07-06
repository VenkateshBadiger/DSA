WITH first_day as(
SELECT player_id, MIN(event_date) as first
FROM Activity
GROUP BY player_id
)
SELECT ROUND(COUNT(DISTINCT f.player_id)/(SELECT count(*) FROM first_day),2) as fraction
FROM Activity a
join first_day f ON f.player_id = a.player_id AND a.event_date = DATE_ADD(f.first, INTERVAL 1 DAY)
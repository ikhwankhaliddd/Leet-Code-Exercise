# Write your MySQL query statement below
SELECT A.player_id, MIN(A.event_date) AS first_login
FROM Activity A
GROUP BY player_id;
with req as 
(
    SELECT c.user_id, COUNT(*) as req
    FROM Confirmations c
    GROUP BY c.user_id
),
con_req as 
(
    SELECT c.user_id, COUNT(*) as con_req
    FROM Confirmations c
    WHERE c.action = 'confirmed'
    GROUP BY c.user_id
)
SELECT s.user_id, ROUND(COALESCE(cr.con_req/r.req, 0),2) confirmation_rate
FROM Signups s
LEFT JOIN req r on r.user_id = s.user_id
LEFT JOIN con_req cr on cr.user_id = s.user_id


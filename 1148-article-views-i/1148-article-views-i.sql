# Write your MySQL query statement below
SELECT id
FROM (
    SELECT DISTINCT author_id AS id
    FROM Views
    WHERE author_id = viewer_id
) t
ORDER BY id;
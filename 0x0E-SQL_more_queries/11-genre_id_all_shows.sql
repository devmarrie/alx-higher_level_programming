-- a script that lists all shows contained in the database
-- we use left join so that it can return null values where it finds no match
SELECT s.`title`, g.`genre_id`
FROM tv_shows as s
    LEFT JOIN `tv_show_genres` as g
    ON s.`id` = g.`show_id`
ORDER BY s.`title`, g.`genre_id`;

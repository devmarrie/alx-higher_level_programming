-- Import the database dump from hbtn_0d_tvshows
-- a script that lists all shows contained in hbtn_0d_tvshows that have at least one genre linked
SELECT tv.`title`, sh.`genre_id`
  FROM `tv_shows` AS tv
        INNER JOIN `tv_show_genres` AS sh
        ON tv.`id` = sh.`show_id`
ORDER BY tv.`title`, sh.`genre_id`;


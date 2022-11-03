--  lists all cities contained in the database hbtn_0d_usa
SELECT `city`.`id`, `city`.`name`, `states`.`name`
  FROM `city`
    INNER JOIN `states`
    ON `city`.`state_id` = `state`.`id` 
ORDER BY `city`.`id`;

SELECT
    CONCAT(a.first_name, ' ',a.last_name),
    CONCAT(LOWER(CONCAT_WS('',LEFT(a.first_name,1),RIGHT(a.last_name,2),LENGTH(a.last_name))),'', '@sm-cast.com'),
    a.awards
FROM
    actors AS a
LEFT JOIN
        productions_actors AS pa
ON
    a.id = pa.actor_id
WHERE
    pa.production_id IS NULL
ORDER BY
    a.awards DESC,
    a.id;
INSERT INTO
    actors(first_name, last_name, birthdate, height,awards, country_id)
SELECT
    reverse(a.first_name),
    reverse(a.last_name),
    a.birthdate - 2 "days",
    COALESCE(a.height, 0) + 10,
    a.country_id,
    (SELECT c.id FROM countries AS c WHERE c.name = 'Armenia')
FROM
    actors AS a
WHERE
    a.id BETWEEN 10 AND 20;
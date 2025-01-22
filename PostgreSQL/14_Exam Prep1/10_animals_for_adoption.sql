SELECT
	a.name AS animal,
	TO_CHAR(a.birthdate, 'YYYY') AS birth_year,
	atp.animal_type
FROM
	animals AS a
JOIN
	animal_types AS atp
ON
	a.animal_type_id = atp.id
WHERE
	atp.animal_type <> 'Birds'
		AND
	AGE('01/01/2022', a.birthdate) < '5 year'
		AND
	a.owner_id IS NULL
ORDER BY
	a.name
;
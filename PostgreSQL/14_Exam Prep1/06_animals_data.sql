SELECT
	a.name,
	atp.animal_type,
	TO_CHAR(a.birthdate, 'DD.MM.YYYY') AS birthdate
FROM
	animals AS a
JOIN
	animal_types AS atp
ON
	atp.id = a.animal_type_id
ORDER BY
	a.name
;
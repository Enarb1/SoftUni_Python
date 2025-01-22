SELECT
	a.name AS address,
	CASE WHEN EXTRACT(HOUR FROM co.start) BETWEEN 6 AND 20 THEN 'Day'
	ELSE 'Night'
	END AS day_time,
	co.bill,
	c.full_name,
	ca.make,
	ca.model,
	cat.name AS category_name
FROM
	clients AS c
JOIN
	courses AS co
ON
	co.client_id = c.id
JOIN
	addresses AS a
ON
	a.id = co.from_address_id
JOIN
	cars AS ca
ON
	ca.id = co.car_id
JOIN
	categories AS cat
ON
	cat.id = ca.category_id
ORDER BY
	co.id
;

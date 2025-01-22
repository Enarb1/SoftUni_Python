SELECT
	c.full_name,
	COUNT(co.car_id) AS count_of_cars,
	SUM(bill) AS total_sum
FROM
	clients AS c
JOIN
	courses AS co
ON
	c.id = co.client_id
GROUP BY
	c.full_name
HAVING
	COUNT(co.car_id) > 1
		AND
	SUBSTRING(c.full_name, 2, 1) = 'a'
ORDER BY
	c.full_name;

SELECT driver_id, vehicle_type,
	CONCAT(c.first_name, ' ', c.last_name) AS driver_name
FROM vehicles AS v
	JOIN campers as c
		ON v.driver_id = c.id;
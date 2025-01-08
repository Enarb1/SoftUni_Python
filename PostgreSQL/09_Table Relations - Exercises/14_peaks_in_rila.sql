SELECT
	mountain_range,
	peak_name,
	elevation
FROM
	peaks AS p
JOIN
	mountains AS m
ON
	p.mountain_id = m.id
WHERE
	mountain_range LIKE '%Rila%'
ORDER BY
	elevation DESC;


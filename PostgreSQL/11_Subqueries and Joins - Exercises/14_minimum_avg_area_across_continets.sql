SELECT
	MIN(avg_area) AS min_average_area
FROM
	(SELECT
		AVG(area_in_sq_km) AS avg_area
	FROM
		countries AS c
	GROUP BY
		c.continent_code) AS min_avg;

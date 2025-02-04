SELECT
  c.name AS country_name,
  COUNT(p.id) AS productions_count,
  COALESCE(AVG(pi.budget), 0) AS avg_budget
FROM
    countries AS c
JOIN
    productions AS p
ON
        p.country_id = c.id
JOIN
    productions_info AS pi
ON
    p.production_info_id = pi.id
GROUP BY
    country_name
ORDER BY
    productions_count DESC,
    country_name;


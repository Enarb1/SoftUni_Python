SELECT
  p.title,
  CASE
    WHEN pi.rating <= 3.50 THEN 'poor'
    WHEN pi.rating > 3.50 AND pi.rating <= 8.00 THEN 'good'
    ELSE 'excellent'
  END AS rating,
  CASE
    WHEN pi.has_subtitles IS TRUE THEN 'Bulgarian'
    ELSE 'N/A'
  END AS subtitles,
  COUNT(pa.actor_id) AS actors_count
FROM
    productions AS p
JOIN
    productions_info AS pi
ON
    p.production_info_id = pi.id
JOIN
    productions_actors AS pa
ON
    p.id = pa.production_id
JOIN
    actors AS a
ON
    pa.actor_id = a.id
GROUP BY
    p.title, pi.rating, pi.has_subtitles
ORDER BY
    rating,
    actors_count DESC,
    p.title;


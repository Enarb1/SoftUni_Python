SELECT
	CONCAT(c.first_name, ' ', c.last_name) AS full_name,
	c.email,
	MAX(bg.rating)
FROM
	board_games AS bg
JOIN
	creators_board_games AS cbg
ON
	cbg.board_game_id = bg.id
JOIN
	creators AS c
ON
	cbg.creator_id = c.id
GROUP BY
	full_name, c.email
HAVING
	c.email LIKE '%.com'
ORDER BY
	full_name ASC
;
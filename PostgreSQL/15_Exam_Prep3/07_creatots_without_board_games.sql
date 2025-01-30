SELECT
	c.id,
	CONCAT(c.first_name, ' ', c.last_name) AS creator_name,
	c.email
FROM
	creators_board_games AS cbg
JOIN
	board_games AS bg
ON
	cbg.board_game_id = bg.id
RIGHT JOIN
	creators AS c
ON
	c.id = cbg.creator_id
WHERE
	cbg.board_game_id IS NULL
;
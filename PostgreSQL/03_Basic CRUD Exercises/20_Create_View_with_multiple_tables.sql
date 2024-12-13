CREATE VIEW
		view_addresses
AS
SELECT
	CONCAT_WS(
	' ',
	e.first_name,
	e.last_name
	) AS full_name,
	e.department_id,
	CONCAT_WS(
	' ',
	a.number,
	a.street
	) AS address

FROM
	employees AS e, addresses AS a
WHERE
	a.id = e.address_id
ORDER BY
	address;
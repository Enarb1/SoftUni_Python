SELECT
	a.name,
	a.country,
	DATE(b.booked_at) AS booked_at
-- b.booked_at ::DATE
FROM
	apartments AS a
LEFT JOIN
	bookings AS b
USING
	(booking_id)
LIMIT 10;
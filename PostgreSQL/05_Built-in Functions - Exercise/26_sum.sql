SELECT
	SUM(booked_for) as total_value
FROM
	bookings
WHERE
	apartment_id = 90

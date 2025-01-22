CREATE OR REPLACE FUNCTION fn_courses_by_client(
	phone_num VARCHAR(20)
) RETURNS INT
AS
$$
DECLARE
	count_of_courses INT;
BEGIN
	SELECT
		COUNT(*)
	INTO
		count_of_courses
	FROM
		clients AS c
	JOIN
		courses AS co
	ON
		c.id = co.client_id
	WHERE
		c.phone_number = phone_num;

	RETURN count_of_courses;
END;
$$
LANGUAGE plpgsql;

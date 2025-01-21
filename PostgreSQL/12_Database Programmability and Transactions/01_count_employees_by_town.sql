CREATE OR REPLACE FUNCTION fn_count_employees_by_town(town_name VARCHAR(20))
RETURNS VARCHAR AS
$$
	DECLARE employee_count INT;
    BEGIN
        SELECT
            COUNT(*)
		INTO
			employee_count
        FROM
            employees AS e
        JOIN
            addresses AS a
        USING
            (address_id)
        JOIN
            towns AS t
        USING
            (town_id)
        WHERE
            t.name = town_name;
		RETURN employee_count;
    END;
$$
LANGUAGE plpgsql
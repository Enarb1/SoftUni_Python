CREATE OR REPLACE FUNCTION fn_get_volunteers_count_from_department(
	searched_volunteers_department VARCHAR(30)
) RETURNS INT
AS
$$
DECLARE
	volunteer_count INT;
BEGIN
	SELECT
		COUNT(*)
	INTO
		volunteer_count
	FROM
		volunteers_departments AS vd
	JOIN
		volunteers AS v
	ON
		v.department_id = vd.id
	WHERE
		vd.department_name = searched_volunteers_department;

	RETURN volunteer_count;
END;
$$
LANGUAGE plpgsql;
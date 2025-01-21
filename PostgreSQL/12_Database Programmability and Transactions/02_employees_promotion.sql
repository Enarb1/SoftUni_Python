CREATE OR REPLACE PROCEDURE sp_increase_salaries(department_name VARCHAR)
       AS
$$
    BEGIN
      UPDATE
	    employees
        SET
	        salary = salary + (salary * 0.05)
        FROM
	        departments AS d
        WHERE
	        employees.department_id = d.department_id
		        AND
	        d.name = department_name ;
    END;
$$
LANGUAGE plpgsql
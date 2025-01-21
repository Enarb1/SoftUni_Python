CREATE OR REPLACE FUNCTION fn_function_name(add variables)
RETURNS 'add type' AS
$$
    BEGIN
        RETURN COUNT()
    END;
$$
LANGUAGE plpgsql
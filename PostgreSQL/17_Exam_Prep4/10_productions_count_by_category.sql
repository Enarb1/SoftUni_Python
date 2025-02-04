CREATE OR REPLACE FUNCTION udf_category_productions_count(
    category_name VARCHAR(50)
)RETURNS TEXT
AS
$$
    DECLARE
        message_text TEXT;
    BEGIN
        SELECT
            FORMAT('Found %s productions.', COUNT(*))
        INTO
            message_text
        FROM
            categories AS c
        JOIN
            categories_productions AS cp
        ON
            c.id = cp.category_id
        JOIN
            productions AS p
        ON
            p.id = cp.production_id
        WHERE
            c.name = category_name;
        RETURN message_text;
    END;
$$
LANGUAGE plpgsql;
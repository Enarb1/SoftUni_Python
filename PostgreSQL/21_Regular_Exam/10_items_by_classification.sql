CREATE OR REPLACE FUNCTION udf_classification_items_count(
    classification_name VARCHAR(30)
) RETURNS TEXT
AS
$$
    DECLARE item_count INTEGER;
    BEGIN
        SELECT
            COUNT(*)
        INTO
            item_count
        FROM
            items AS i
        JOIN
            classifications AS cs
        ON i.classification_id = cs.id
        WHERE
            cs.name = classification_name;

        IF item_count > 0 THEN
            RETURN FORMAT('Found %s items.', item_count);
        ELSE
            RETURN 'No items found.';
        END IF;
    END;
$$
LANGUAGE plpgsql;
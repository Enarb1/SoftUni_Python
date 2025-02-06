CREATE OR REPLACE PROCEDURE sp_customer_country_name(
    customer_full_name VARCHAR(50),
    OUT customer_country VARCHAR(50)
)
AS
$$
    BEGIN
        SELECT
           co.name
        INTO
            customer_country
        FROM
            customers AS c
        JOIN
            countries AS co ON c.country_id = co.id
        WHERE
            CONCAT(c.first_name, ' ', last_name) = customer_full_name;
    END;
$$
LANGUAGE plpgsql;
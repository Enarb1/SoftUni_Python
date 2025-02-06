CREATE OR REPLACE FUNCTION fn_feedbacks_for_product(
    product_name VARCHAR(25)
)
RETURNS TABLE(
    customer_id INTEGER,
    customer_name VARCHAR (75),
    feedback_description VARCHAR(255),
    feedback_rate NUMERIC(4,2)
)
AS
$$
    BEGIN
       RETURN QUERY
                SELECT
                    c.id AS customer_id,
                    c.first_name AS customer_name,
                    f.description AS feedback_description,
                    f.rate AS feedback_rate
                FROM
                    products AS p
                JOIN
                    feedbacks AS f ON p.id = f.product_id
                JOIN
                    customers AS c ON f.customer_id = c.id
                WHERE
                    p.name = product_name
                ORDER BY
                    c.id;
    END;
$$
LANGUAGE plpgsql;
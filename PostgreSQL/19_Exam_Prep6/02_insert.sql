CREATE TABLE gift_recipients(
    id SERIAL PRIMARY KEY,
    name VARCHAR(75),
    country_id INTEGER NOT NULL,
    gift_sent BOOLEAN DEFAULT FALSE
);

INSERT INTO
    gift_recipients(name,country_id)
SELECT
    CONCAT(first_name, ' ', last_name),
    country_id
FROM
    customers
;

UPDATE
    gift_recipients
SET
    gift_sent = TRUE
WHERE
    country_id IN ( 7, 8, 14, 17, 26)
;
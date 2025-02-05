CREATE OR REPLACE PROCEDURE udp_modify_account(
    address_street VARCHAR(30), address_town VARCHAR(30)
)
AS
$$
    BEGIN
        UPDATE
            accounts
        SET
            job_title =
            CONCAT('(Remote) ',job_title )
        WHERE
            id IN (SELECT a.id
                FROM accounts AS a
                JOIN addresses AS ad ON a.id = ad.account_id
                WHERE ad.street = address_street
                        AND ad.town = address_town);
    END;
$$
LANGUAGE plpgsql
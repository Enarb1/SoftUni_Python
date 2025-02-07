CREATE OR REPLACE PROCEDURE sp_players_team_name(
    IN player_name VARCHAR(50),
    OUT team_name VARCHAR(45)
)
AS
$$
    BEGIN
        SELECT
            CASE
                WHEN t.name IS NULL THEN 'The player currently has no team'
                ELSE t.name
            END
        INTO
            team_name
        FROM
            players AS p
        LEFT JOIN
                teams AS t
        ON p.team_id = t.id
        WHERE
            CONCAT(p.first_name,' ',p.last_name) = player_name;
    END;
$$
LANGUAGE plpgsql;
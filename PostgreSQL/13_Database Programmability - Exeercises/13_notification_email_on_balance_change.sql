CREATE TABLE IF NOT EXISTS notification_emails(
	 id SERIAL PRIMARY KEY,
	 recipient_id INT,
	 subject VARCHAR(255),
	 body TEXT
);

CREATE OR REPLACE FUNCTION
	trigger_fn_send_email_on_balance_change()
RETURNS TRIGGER AS
$$
BEGIN
	INSERT INTO
		notification_email(recipient_id, subject, body)
	VALUES(
		NEW.account_id,
		'Balance change for account: ' || NEW.account_id,
	    CONCAT_WS(' ', 'On', DATE(NOW()), 'your balance was changed from', NEW.old_sum, 'to', NEW.new_sum, '.')
		--OR 'On' || DATE(NOW()) || 'your balance was changed from' || NEW.old_sum || 'to' || NEW.new_sum || '.'
	);
	RETURN NEW;
END;
$$
LANGUAGE plpgsql;

CREATE OR REPLACE TRIGGER
	tr_send_email_on_balance_change
AFTER UPDATE ON
	logs
FOR EACH ROW
WHEN
	(OLD.new_sum <> NEW.new_sum)
EXECUTE FUNCTION
	trigger_fn_send_email_on_balance_change();
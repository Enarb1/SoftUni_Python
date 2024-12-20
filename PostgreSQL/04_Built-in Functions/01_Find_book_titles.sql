SELECT
	title
FROM books
WHERE SUBSTRING(title, 1, 3) = 'The'

--or
--SELECT
--	title
--FROM books
--WHERE left(title, 3) = 'The'
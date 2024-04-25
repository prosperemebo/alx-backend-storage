-- SQL script that creates a stored procedure AddBonus that adds a new correction for a student.
DELIMITER $$

CREATE PROCEDURE ADDBONUS(
	IN user_id INT,
	IN project_name VARCHAR(225),
	IN score FLOAT
)
BEGIN
	IF NOT EXISTS (
		SELECT
			*
		FROM
			projects
		WHERE
			name = project_name
	) THEN
		INSERT INTO projects (
			name
		) VALUES (
			project_name
		);
	END IF;

	SET @id = (
		SELECT
			id
		FROM
			projects
		WHERE
			NAME = project_name
	);
	INSERT INTO corrections (
		user_id,
		project_id,
		score
	) VALUES (
		user_id,
		@id,
		score
	);
END $$ DELIMITER;

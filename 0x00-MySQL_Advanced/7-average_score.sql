-- a SQL script that creates a stored procedure ComputeAverageScoreForUser
-- that computes and store the average score for a student

DELIMITER //
DROP PROCEDURE IF EXISTS ComputeAverageScoreForUser;

CREATE PROCEDURE ComputeAverageScoreForUser(user_id INT)
BEGIN
	DECLARE total_score INT;
	DECLARE project_count INT;
	DECLARE average FLOAT;

	-- get user score
	SELECT SUM(score) INTO total_score FROM corrections WHERE corrections.user_id = user_id;
	SELECT COUNT(*) INTO project_count FROM corrections WHERE corrections.user_id = user_id;

	-- Calculate the average score
    	SET average = total_score / project_count;

	-- update user average score
	UPDATE users
	SET average_score = average
	WHERE id = user_id;
END;
//

DELIMITER ;

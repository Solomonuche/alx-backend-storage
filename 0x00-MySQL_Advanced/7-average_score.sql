-- a SQL script that creates a stored procedure ComputeAverageScoreForUser
-- that computes and store the average score for a student

DELIMITER //

CREATE PROCEDURE ComputeAverageScoreForUser(user_id INT)
BEGIN
	DECLARE user_score INT;

	-- get user score
	SELECT AVG(score) INTO user_score FROM corrections WHERE user_id = user_id;

	-- update user average score
	UPDATE users
	SET average_score = user_score
	WHERE id = user_id;
END;
//

DELIMITER ;

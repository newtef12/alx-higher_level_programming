-- Create the users if they don't exist
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost';
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost';

-- Grant some privileges to the users for demonstration purposes
GRANT SELECT, INSERT, UPDATE ON *.* TO 'user_0d_1'@'localhost';
GRANT SELECT ON *.* TO 'user_0d_2'@'localhost';

-- Show privileges for user_0d_1
SHOW GRANTS FOR 'user_0d_1'@'localhost';

-- Show privileges for user_0d_2
SHOW GRANTS FOR 'user_0d_2'@'localhost';

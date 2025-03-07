-- Creates the MySQL server user
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost'
IDENTIFIED BY 'user_0d_1_pwdP@ssw0rd!';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost'
WITH GRANT OPTION;
FLUSH PRIVILEGES;

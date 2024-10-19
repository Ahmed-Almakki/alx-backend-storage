-- creates a table users
CREATE TABLE if not EXISTS users (
	id INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
	email CHAR(255) NOT NULL UNIQUE,
	name CHAR(255)
	)

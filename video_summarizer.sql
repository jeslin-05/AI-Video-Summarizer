CREATE DATABASE IF NOT EXISTS video_summarizer;
USE video_summarizer;

CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    mobile_number VARCHAR(15) NOT NULL
);

-- Default Admin User
INSERT INTO users (username, password, mobile_number) 
VALUES ('admin', '12345678', '0000000000')
ON DUPLICATE KEY UPDATE username=username;
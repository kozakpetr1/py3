CREATE DATABASE IF NOT EXISTS secure_messaging;
USE secure_messaging;

CREATE TABLE Users (
    user_id CHAR(36) NOT NULL PRIMARY KEY,
    username VARCHAR(255) NOT NULL UNIQUE,
    public_key TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    last_seen TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

CREATE TABLE Messages (
    message_id CHAR(36) NOT NULL PRIMARY KEY,
    sender_id CHAR(36) NOT NULL,
    receiver_id CHAR(36) NOT NULL,
    encrypted_message TEXT NOT NULL,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    status ENUM('sent', 'delivered', 'read') DEFAULT 'sent',
    FOREIGN KEY (sender_id) REFERENCES Users(user_id) ON DELETE CASCADE,
    FOREIGN KEY (receiver_id) REFERENCES Users(user_id) ON DELETE CASCADE
);

INSERT INTO Users (user_id, username) VALUES
('123e4567-e89b-12d3-a456-426614174000', 'Alice'),
('223e4567-e89b-12d3-a456-426614174000', 'Bob');

INSERT INTO Messages (message_id, sender_id, receiver_id, encrypted_message, status) VALUES
('64d2c8f0-4385-4a7d-8a2b-e789f6bfc7c2', '123e4567-e89b-12d3-a456-426614174000', '223e4567-e89b-12d3-a456-426614174000', 'gAAAAABhmltx2...', 'sent');

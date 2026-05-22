-- ─────────────────────────────────────────────────────────
-- Portfolio DB Setup
-- Run this file once in MySQL Workbench or terminal:
--   mysql -u root -p < setup_db.sql
-- ─────────────────────────────────────────────────────────

CREATE DATABASE IF NOT EXISTS portfolio_db
  CHARACTER SET utf8mb4
  COLLATE utf8mb4_unicode_ci;

USE portfolio_db;

CREATE TABLE IF NOT EXISTS contacts (
    id           INT AUTO_INCREMENT PRIMARY KEY,
    first_name   VARCHAR(100)  NOT NULL,
    last_name    VARCHAR(100),
    email        VARCHAR(200)  NOT NULL,
    subject      VARCHAR(255),
    message      TEXT          NOT NULL,
    submitted_at DATETIME      DEFAULT CURRENT_TIMESTAMP
);

-- Optional: view all messages
-- SELECT * FROM contacts ORDER BY submitted_at DESC;

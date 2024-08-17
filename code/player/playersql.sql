CREATE DATABASE player_ranking_db;
grant select, insert, update on player_ranking_db.* to 'jackmanimation'@'%' with grant option;

USE player_ranking_db;

CREATE TABLE players (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    rating FLOAT DEFAULT 1000,
    games_played INT DEFAULT 0,
    games_won INT DEFAULT 0,
    games_lost INT DEFAULT 0,
    games_percentage FLOAT DEFAULT 0
);

-- Example inserts
INSERT INTO players (name) VALUES ('Player 1');
INSERT INTO players (name) VALUES ('Player 2');
INSERT INTO players (name) VALUES ('Player 3');
INSERT INTO players (name) VALUES ('Player 4');
INSERT INTO players (name) VALUES ('Player 5');
INSERT INTO players (name) VALUES ('Denis Jackman');
INSERT INTO players (name) VALUES ('Xavier Jackman');

-- Select all players
SELECT * FROM players;

import mysql.connector

# Database connection setup
db_connection = mysql.connector.connect(
    host="localhost",
    user="yourusername",
    password="yourpassword",
    database="player_ranking_db"
)

db_cursor = db_connection.cursor()

# Constants
K = 32  # K-factor in ELO rating system

# Function to calculate expected score
def calculate_expected_score(rating_a, rating_b):
    expected_a = 1 / (1 + 10 ** ((rating_b - rating_a) / 400))
    return expected_a

# Function to update ratings after a match
def update_ratings(player_a_id, player_b_id, result):
    # Retrieve current ratings
    db_cursor.execute("SELECT rating FROM players WHERE id = %s", (player_a_id,))
    rating_a = db_cursor.fetchone()[0]
    
    db_cursor.execute("SELECT rating FROM players WHERE id = %s", (player_b_id,))
    rating_b = db_cursor.fetchone()[0]
    
    # Calculate expected scores
    expected_a = calculate_expected_score(rating_a, rating_b)
    expected_b = calculate_expected_score(rating_b, rating_a)
    
    # Update ratings based on result
    new_rating_a = rating_a + K * (result - expected_a)
    new_rating_b = rating_b + K * ((1 - result) - expected_b)
    
    # Update ratings in the database
    db_cursor.execute("UPDATE players SET rating = %s, games_played = games_played + 1, games_won = games_won + %s WHERE id = %s",
                      (new_rating_a, result, player_a_id))
    
    db_cursor.execute("UPDATE players SET rating = %s, games_played = games_played + 1, games_won = games_won + %s WHERE id = %s",
                      (new_rating_b, 1 - result, player_b_id))
    
    db_connection.commit()

# Example usage
update_ratings(1, 2, 1)  # Player 1 wins against Player 2
update_ratings(2, 3, 0)  # Player 2 loses against Player 3

# Close database connection
db_cursor.close()
db_connection.close()

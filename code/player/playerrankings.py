''' Module to calculate player ranK_FACTORings using ELO rating system'''
import os
import sys
import mysql.connector as mysql

# pylint: disable=C0413
sys.path.append(os.path.realpath('../..'))
from jackmanimation.gameitems.gamefunctions import credscheck

# Constants
K_FACTOR = 32  # k-factor in ELO rating system
SECRETS_FILE = 'Z:/pyproject/secrets/secrets.json'


def main():
    ''' Main function to calculate expected score'''
    print("[+] Starting to Calculate player rankings")
    dbredid = credscheck(SECRETS_FILE)
    # Database connection setup
    mysqlusername = dbredid["MySQLUsername"]
    mysqlpassword = dbredid["MySQLPassword"]
    mysqlhostname = dbredid["arthur"]

    print("[-] Connecting to database")
    use_db = mysql.connect(host=mysqlhostname,
                           user=mysqlusername,
                           password=mysqlpassword,
                           database='player_ranking_db')
    print("[-] Connected to database")
    print("[-] Calculating player rankings")
    db_cursor = use_db.cursor()
    # Example usage
    print("[-] Example usage of updating player rankings")
    print("[-] Player 1 wins against Player 2")
    update_ratings(db_cursor, use_db, 1, 2, 1)  # Player 1 wins against Player 2
    print("[-] Player 2 loses against Player 3")
    update_ratings(db_cursor, use_db, 2, 3, 0)  # Player 2 loses against Player 3
    print("[-] Player 3 loses against Player 2")
    update_ratings(db_cursor, use_db, 3, 2, 0)  # Player 2 loses against Player 3
    print("[-] Player 3 loses against Player 1")
    update_ratings(db_cursor, use_db, 4, 1, 0)  # Player 2 loses against Player 3
    update_ratings(db_cursor, use_db, 4, 2, 0)  # Player 2 loses against Player 3
    update_ratings(db_cursor, use_db, 4, 3, 0)  # Player 2 loses against Player 3
    update_ratings(db_cursor, use_db, 4, 1, 0)  # Player 2 loses against Player 3
    update_ratings(db_cursor, use_db, 4, 2, 0)  # Player 2 loses against Player 3

    # Close database connection
    print("[-] Closing database connection")
    db_cursor.close()
    use_db.close()
    print("[+] Finished Calculating player rankings")


def calculate_expected_score(rating_a, rating_b):
    ''' Function to calculate expected score'''
    expected_a = 1 / (1 + 10 ** ((rating_b - rating_a) / 400))
    return expected_a


def update_ratings(ur_cursor, ur_connection, player_a_id, player_b_id, result):
    ''' Function to calculate expected score'''
    # Retrieve current ratings
    ur_cursor.execute("SELECT rating FROM players WHERE id = %s", (player_a_id,))
    ur_rating_a = ur_cursor.fetchone()[0]

    ur_cursor.execute("SELECT rating FROM players WHERE id = %s", (player_b_id,))
    ur_rating_b = ur_cursor.fetchone()[0]

    # Calculate expected scores
    expected_a = calculate_expected_score(ur_rating_a, ur_rating_b)
    expected_b = calculate_expected_score(ur_rating_b, ur_rating_a)

    # Update ratings based on result
    new_rating_a = ur_rating_a + K_FACTOR * (result - expected_a)
    new_rating_b = ur_rating_b + K_FACTOR * ((1 - result) - expected_b)

    # Update ratings in the database
    ur_cursor.execute("UPDATE players SET rating = %s, games_played = games_played + 1, games_won = games_won + %s WHERE id = %s",
                      (new_rating_a, result, player_a_id))

    ur_cursor.execute("UPDATE players SET rating = %s, games_played = games_played + 1, games_won = games_won + %s WHERE id = %s",
                      (new_rating_b, 1 - result, player_b_id))

    ur_connection.commit()


if __name__ == "__main__":
    main()

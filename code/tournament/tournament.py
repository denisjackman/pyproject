''' tournament modeller'''
import random

# Initialize PLAYERS with 5 lives each
PLAYERS = {"P1": 5, "P2": 5, "P3": 5, "P4": 5, "P5": 5, "P6": 5, "P7": 5, "P8": 5}
MATCHES_PLAYED = {}


def find_opponent(fo_player, fo_players, fo_matches_played):
    ''' Function to find the best match for a player '''
    available_opponents = [p for p, lives in fo_players.items() if p != fo_player and lives > 0 and fo_matches_played[fo_player][p] == 0]
    print(f"[0] {available_opponents} {fo_players} {fo_matches_played}")
    if available_opponents:
        return available_opponents[0]  # Return first available opponent who hasn't played against this player
    # If no new opponents are available, find any player who is still in the game
    return [p for p, lives in fo_players.items() if p != fo_player and lives > 0][0]


def main():
    ''' main '''
    # Initialize MATCHES_PLAYED dictionary
    for p1 in PLAYERS:
        MATCHES_PLAYED[p1] = {p2: 0 for p2 in PLAYERS if p2 != p1}

    # Tournament simulation
    while len([p for p, lives in PLAYERS.items() if lives > 0]) > 1:
        round_matches = []
        round_players = [p for p, lives in PLAYERS.items() if lives > 0]
        # Pair PLAYERS for the round
        while len(round_players) > 1:
            print(f"[-] prematch {round_players} {round_matches}")
            p1 = round_players.pop(0)
            p2 = find_opponent(p1, PLAYERS, MATCHES_PLAYED)
            print(f"[=] {p1} {p2}")
            round_players.remove(p2)
            round_matches.append((p1, p2))

        # Process each match
        for p1, p2 in round_matches:
            # Simulate match (random loser)
            loser = random.choice([p1, p2])
            PLAYERS[loser] -= 1
            MATCHES_PLAYED[p1][p2] += 1
            MATCHES_PLAYED[p2][p1] += 1
            print(f"{p1} vs {p2}: {loser} loses a life. Lives remaining: {PLAYERS[loser]}")

    # Determine the winner
    winner = [p for p, lives in PLAYERS.items() if lives > 0][0]
    print(f"Winner of the tournament: {winner}")


if __name__ == "__main__":
    main()

import random

def roll():
    min_value = 1
    max_value = 6
    return random.randint(min_value, max_value)

    return roll 

    # Get number of players
while True:
    players = input("Enter the number of players (2-5): ")
    if players.isdigit(): 
        players = int(players)
        if 2 <= players <= 5:
            break
        else:
            print("Must be between 2 and 5 players.")
    else:
        print("Invalid input. Please enter a number.")

    # Get custom max score
while True:
    max_score = input("Enter the winning score (default 55): ").strip()
    if max_score == "":
        max_score = 55
        break
    elif max_score.isdigit() and int(max_score) > 0:
        max_score = int(max_score)
        break
    else:
        print("Invalid input. Please enter a positive number or leave blank for default.")

print(f"Starting the game with {players} players! First to {max_score} wins!\n")

player_scores = [0 for _ in range(players)]

    # Simulate turn and track score
while max(player_scores) < max_score:
    for player_idx in range(players):
        print("\nPlayer", player_idx + 1, "turn has just started!")
        print("Your total score is:", player_scores[player_idx], "\n")
        current_score = 0

        while True:
            should_roll = input("Do you want to roll the dice? (y/n): ").strip().lower()
            if should_roll != "y":
                break

            value = roll()
            if value == 1:
                next_player = (player_idx + 1) % players + 1
                print(f"You rolled a 1! Player {next_player}, is next!\n")
                current_score = 0
                break
            else:
                current_score += value
                print("You rolled a:", value)

            print("Your score is:", current_score)

        player_scores[player_idx] += current_score
        print("Your total score is:", player_scores[player_idx])

        # Show scoreboard after each round
        print("\n--- Scoreboard ---")
        for idx, score in enumerate(player_scores):
            print(f"Player {idx+1}: {score}")
        print("------------------\n")

# After the game ends, show results
winners = [i+1 for i, score in enumerate(player_scores) if score >= max_score]
if len(winners) == 1:
    print(f"\nPlayer {winners[0]} wins with a score of {player_scores[winners[0]-1]}!\n")
else:
    print(f"\nIt's a tie between players {', '.join(map(str, winners))}!")
    print("Final scores:", player_scores)

print("Game over! Final scores:", player_scores, "\n")



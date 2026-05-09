import random


def play(player1, player2, num_games, verbose=False):

    p1_prev_play = ""
    p2_prev_play = ""

    results = {"p1": 0, "p2": 0, "tie": 0}

    for _ in range(num_games):

        p1_play = player1(p2_prev_play)
        p2_play = player2(p1_prev_play)

        if p1_play == p2_play:
            results["tie"] += 1

            winner = "Tie."
        elif (
                (p1_play == "P" and p2_play == "R")
                or (p1_play == "R" and p2_play == "S")
                or (p1_play == "S" and p2_play == "P")):

            results["p1"] += 1
            winner = "Player 1 wins."
        elif p2_play == "R" and p1_play == "S":
            results["p2"] += 1
            winner = "Player 2 wins."
        elif p2_play == "S" and p1_play == "P":
            results["p2"] += 1
            winner = "Player 2 wins."
        elif p2_play == "P" and p1_play == "R":
            results["p2"] += 1
            winner = "Player 2 wins."

        if verbose:
            print("Player 1:", p1_play, "| Player 2:", p2_play)
            print(winner)
            print()

        p1_prev_play = p1_play
        p2_prev_play = p2_play

    games_won = results['p1']

    win_rate = games_won / num_games * 100

    print("Final results:", results)
    print(f"Player 1 win rate: {win_rate}%")

    return (win_rate >= 60)


def quincy(prev_play,
           counter=[0]):

    counter[0] += 1
    choices = ["R", "R", "P", "P", "S"]
    return choices[counter[0] % len(choices)]


def abbey(prev_opponent_play,
          opponent_history=[]):

    opponent_history.append(prev_opponent_play)

    last_two = "".join(opponent_history[-2:])

    play_order = {
        "RR": 0,
        "RP": 0,
        "RS": 0,
        "PR": 0,
        "PP": 0,
        "PS": 0,
        "SR": 0,
        "SP": 0,
        "SS": 0,
    }

    for i in range(len(opponent_history) - 2):
        sequence = "".join(opponent_history[i:i + 2])

        if sequence in play_order:
            play_order[sequence] += 1

    potential_plays = [
        last_two + "R",
        last_two + "P",
        last_two + "S",
    ]

    sub_order = {
        k: play_order.get(k[:2], 0)
        for k in potential_plays
    }

    prediction = max(sub_order,
                     key=sub_order.get)[-1:]

    ideal_response = {
        "P": "S",
        "R": "P",
        "S": "R"
    }

    return ideal_response[prediction]


def kris(prev_opponent_play):
    if prev_opponent_play == "":
        prev_opponent_play = random.choice(["R", "P", "S"])

    ideal_response = {
        "P": "S",
        "R": "P",
        "S": "R"
    }

    return ideal_response[prev_opponent_play]


def mrugesh(prev_opponent_play,
            opponent_history=[]):

    opponent_history.append(prev_opponent_play)

    if len(opponent_history) <= 10:
        return random.choice(["R", "P", "S"])

    last_ten = opponent_history[-10:]

    most_frequent = max(set(last_ten),
                        key=last_ten.count)

    ideal_response = {
        "P": "S",
        "R": "P",
        "S": "R"
    }

    return ideal_response[most_frequent]
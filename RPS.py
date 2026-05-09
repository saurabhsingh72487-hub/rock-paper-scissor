import random

def player(prev_play,
           opponent_history=[],
           my_history=[]):

    # Reset histories for new match
    if prev_play == "":
        opponent_history.clear()
        my_history.clear()

    opponent_history.append(prev_play)

    # Winning counters
    ideal_response = {
        "R": "P",
        "P": "S",
        "S": "R"
    }

    # First move
    if prev_play == "":
        move = "R"
        my_history.append(move)
        return move

    # ------------------------------------------------
    # Detect KRIS
    # Kris always plays counter to our previous move
    # ------------------------------------------------

    if len(my_history) >= 1:

        expected = ideal_response[my_history[-1]]

        # If opponent likely is Kris
        if prev_play == expected:

            # Kris predicts our next move based on previous
            # So we play the counter of Kris's expected move
            move = ideal_response[expected]

            my_history.append(move)
            return move

    # ------------------------------------------------
    # Pattern Matching Strategy
    # ------------------------------------------------

    if len(opponent_history) > 5:

        pattern = "".join(opponent_history[-5:])

        possibilities = []

        for i in range(len(opponent_history) - 5):

            seq = "".join(opponent_history[i:i+5])

            if seq == pattern:
                possibilities.append(opponent_history[i+5])

        if possibilities:

            prediction = max(set(possibilities),
                             key=possibilities.count)

            move = ideal_response[prediction]

            my_history.append(move)
            return move

    # ------------------------------------------------
    # Frequency Analysis
    # ------------------------------------------------

    count = {
        "R": opponent_history.count("R"),
        "P": opponent_history.count("P"),
        "S": opponent_history.count("S")
    }

    prediction = max(count, key=count.get)

    move = ideal_response[prediction]

    my_history.append(move)

    return move
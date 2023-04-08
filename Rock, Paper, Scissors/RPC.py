def play_game():
    while True:
        fplayer = input("You are Player 1. Rock, Paper, Scissors. Pick one: ").lower()
        splayer = input("You are Player 2. Rock, Paper, Scissors. Pick one: ").lower()

        fwin = "Player 1 wins. "
        swin = "Player 2 wins. "

        if fplayer not in ["rock", "paper", "scissors"] or splayer not in ["rock", "paper", "scissors"]:
            print("Invalid input. Please enter 'rock', 'paper', or 'scissors'.")
            continue

        def compare(p1, p2):
            if p1 == p2:
                return "It's a tie. "
            elif p1 == "rock":
                if p2 == "scissors":
                    return fwin
                else:
                    return swin

            elif p1 == "scissors":
                if p2 == "rock":
                    return swin
                else:
                    return fwin

            elif p1 == "paper":
                if p2 == "rock":
                    return fwin
                else:
                    return swin

        result = compare(fplayer, splayer)
        print(result)

        ask = input("Do you want to play again? y/n: ")
        if ask.lower() == "y":
            continue
        else:
            return 'Thank you for playing.'


print(play_game())

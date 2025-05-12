import random

emoji = {"s": "✂️", "r": "🪨", "p": "📃"}
choice = ["r", "p", "s"]

while True:
    user_score = 0
    computer_score = 0
    round_number = 1

    print("\n🎮 Best of 3 -\n First to 2 Wins!\n")

    while user_score < 2 and computer_score < 2:
        print(f"\nRound {round_number}")
        user_choice = input("Rock, Paper or Scissors (r, p, s)? ").lower()

        if user_choice not in choice:
            print("Invalid choice. Please try again.")
            continue

        computer_choice = random.choice(choice)

        print(f"You chose {emoji[user_choice]}")
        print(f"Computer chose {emoji[computer_choice]}")

        if user_choice == computer_choice:
            print("It's a tie!")
        elif (
            (user_choice == "r" and computer_choice == "s") or
            (user_choice == "p" and computer_choice == "r") or
            (user_choice == "s" and computer_choice == "p")
        ):
            print("You win this round!")
            user_score += 1
        else:
            print("Computer wins this round!")
            computer_score += 1

        print(f"Score - You: {user_score}, Computer: {computer_score}")
        round_number += 1

    # Final winner
    if user_score == 2:
        print("\n🏆 Congratulations! You are the overall winner!")
    else:
        print("\n🤖 The computer wins the best of 3. Better luck next time!")

    # Ask to play again
    want_continue = input("Do you want to play another match? (y/n): ").lower()
    if want_continue == "n":
        print("Thanks for playing!")
        break

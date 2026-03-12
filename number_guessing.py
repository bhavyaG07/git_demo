import random

def play_game():
    number = random.randint(1, 100)
    attempts = 0
    max_attempts = 8
    print("Guess a number between 1 and 100")
    print("You have", max_attempts, "attempts")

    while attempts < max_attempts:
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Enter a valid number")
            continue

        attempts += 1
        if guess == number:
            print("Guessed it right in", attempts, "attempts")
            break
        elif guess > number:
            print("Too high")
        else:
            print("Too low")

        print("Attempts left:", max_attempts - attempts)

    if attempts == max_attempts and guess != number:
        print("Game over. The number was", number)


play_game()
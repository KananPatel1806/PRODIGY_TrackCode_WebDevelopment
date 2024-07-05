import random
def guess_number_game():
    print("Welcome to the Number Guessing Game!")
    print("I have chosen a number between 1 and 100. Try to guess it!")

    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            # Prompt user for a guess
            guess = int(input("Enter your guess (between 1 and 100): "))
            attempts += 1
            
            # Compare the guess with the secret number
            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the number {secret_number} correctly!")
                print(f"It took you {attempts} attempts to win the game.")
                break
        
        except ValueError:
            print("Invalid input. Please enter a valid number.")
if __name__ == "__main__":
    guess_number_game()





    

def guess_my_number():

    start = 1
    end = 1000
    attempts = 0

    print("Think of a number between 1 and 1000 and I will try to guess it in 10 attempts.")

    while attempts < 10:
        # Calculate the guess by finding the middle of the range
        guess = (start + end) // 2
        attempts += 1

        print(f"Attempt {attempts}: Is your number {guess}?")

        # Get user feedback
        user_response = input("Enter 'Too small', 'Too big' or 'You win': ").strip().lower()

        # If the guess is too small, adjust the range to guess higher
        if user_response == "too small":
            start = guess + 1
        # If the guess is too big, adjust the range to guess lower
        elif user_response == "too big":
            end = guess - 1
        # If the guess is correct, end the game
        elif user_response == "you win":
            print(f"Yay! I guessed your number in {attempts} attempts!")
            break
        # In case the input is invalid
        else:
            print(f"Sorry, I didn't understand {user_response}. Please type 'Too small', 'Too big', or 'You win'.")

        # Check if the range is invalid (which could indicate cheating or an error)
        if start > end:
            print("Please make sure you're not cheating!")
            break

    # If the loop ends after 10 attempts and no correct guess
    if attempts == 10:
        print("I couldn't guess the number in 10 attempts.")

if __name__ == "__main__":
    guess_my_number()
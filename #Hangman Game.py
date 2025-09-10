# Hangman Game (Text-Based)
# Task Requirements:
# Use a small list of 5 predefined words
# Limit incorrect guesses to 6
# Use random, while loop, if-else, strings, lists
# Console input/output only (no graphics/audio)

import random

# Step 1: Predefined word list
words = ["apple", "house", "music", "ocean", "happy"]

# Step 2: Randomly choose a word from the list and convert to uppercase
secret_word = random.choice(words).upper()

# Step 3: Create a list of underscores (same length as the secret word)
guessed_word = ["_"] * len(secret_word)

# Step 4: Initialize counters and storage
max_wrong_guesses = 6           # maximum allowed wrong attempts
wrong_guesses = 0               # current number of wrong attempts
guessed_letters = []            # all letters guessed by the player

# Step 5: Welcome message
print("Welcome to Hangman!")
print("Guess the word one letter at a time.")
print(f"You can make {max_wrong_guesses} wrong guesses.\n")

# Step 6: Main game loop
while True:
    # Show current progress (before asking input)
    print("Word:", " ".join(guessed_word))
    print(f"Wrong guesses: {wrong_guesses}/{max_wrong_guesses}")
    print(f"Guessed letters: {', '.join(guessed_letters)}\n")

    # Ask player for a guess
    guess = input("Enter a letter: ").upper()

    # Validate guess (must be a single alphabetic letter)
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single valid letter!\n")
        continue

    # Check if already guessed
    if guess in guessed_letters:
        print("You already guessed that letter!\n")
        continue

    # Add guess to guessed_letters list
    guessed_letters.append(guess)

    # Step 7: Check guess against secret word
    if guess in secret_word:
        print(f"Good guess! {guess} is in the word.\n")
        # Replace underscores with the correct letter
        for i in range(len(secret_word)):
            if secret_word[i] == guess:
                guessed_word[i] = guess
    else:
        print(f" Wrong guess! {guess} is not in the word.\n")
        wrong_guesses += 1   # increase counter for wrong attempts

    #  Show updated progress AFTER checking guess
    print("Word:", " ".join(guessed_word))
    print(f"Wrong guesses: {wrong_guesses}/{max_wrong_guesses}")
    print(f"Guessed letters: {', '.join(guessed_letters)}\n")

    # Step 8: Check win condition
    if "_" not in guessed_word:
        print("Congratulations! You guessed the word!")
        print(f"The word was: {secret_word}")
        break

    # Step 9: Check lose condition
    if wrong_guesses >= max_wrong_guesses:
        print("Game Over! You lost!")
        print(f"The word was: {secret_word}")
        break


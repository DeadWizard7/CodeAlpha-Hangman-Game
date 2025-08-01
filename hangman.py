import random

# List of predefined words
word_list = ['apple', 'banana', 'mango', 'cherry','grape']

# Randomly choose a word
secret_word = random.choice(word_list)
guessed_letters = []
tries = 6

print("Welcome to Hangman!")
print("Hint: The word contains with fruits name!")
print(f"You have {tries} incorrect guesses.Good luck!")

# Create a display of underscores
display_word = ["_" for _ in secret_word]

# Game loop
while tries > 0 and "_" in display_word:
    print("\nCurrent word: " + " ".join(display_word))
    guess = input("Please guess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in secret_word:
        print("You are Correct!")
        for i, letter in enumerate(secret_word):
            if letter == guess:
                display_word[i] = guess
    else:
        tries -= 1
        print(f"Incorrect! Tries left: {tries}")

# Final result
if "_" not in display_word:
    print("\n You won! The word was:", secret_word)
else:
    print("\n Game over! The word was:", secret_word)

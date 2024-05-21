import random

# Define words to guess from
words = ["python", "programming", "computer", "github", "repository"]

# Choose a random word
secret_word = random.choice(words)

# Initialize variables
guesses = []
max_guesses = 8

print("Welcome to the Guessing Game!")

# Game loop
while len(guesses) < max_guesses:
  # Get user input
  guess = input("Guess a letter (or the whole word): ").lower()

  # Check for valid guess
  if len(guess) > 1 and guess != secret_word:
    print("Please guess a single letter or the entire word.")
    continue

  # Check if guess is correct
  if guess == secret_word:
    print(f"Congratulations! You guessed the word '{secret_word}'")
    break
  elif guess in guesses:
    print(f"You already guessed the letter '{guess}'. Try again.")
  elif guess in secret_word:
    print(f"Good guess! '{guess}' is in the word.")
    guesses.append(guess)
  else:
    print(f"Sorry, '{guess}' is not in the word.")
    guesses.append(guess)

  # Display current guess progress (optional)
  guessed_letters = "".join([letter if letter in guesses else "_" for letter in secret_word])
  print(f"Current guess: {guessed_letters}")

# Game over message
if len(guesses) == max_guesses:
  print(f"You ran out of guesses. The word was '{secret_word}'.")

print("Thanks for playing!")

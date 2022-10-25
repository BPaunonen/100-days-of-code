import random
from hangman_words import word_list
from hangman_art import stages, logo


end_of_game = False
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
lives = 6


print(logo)
display = []
for _ in range(word_length):
    display += "_"
print(chosen_word)
while not end_of_game:
    guess = input("Guess a letter: ").lower()
    if guess in display:
      print(f"You've already guessed the letter {guess}.")
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    if guess not in chosen_word:
      print(f"The letter {guess} is not in the word, you lose a life")
      lives -= 1
      print(stages[lives])
      if lives == 0:
        end_of_game = True
        print("You lose")
    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You win.")
  
    
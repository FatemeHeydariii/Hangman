import random

from hangman_words import words_list
from hangman_art import stages
from hangman_art import logo

lives = 6

print(logo)

chosen_word = random.choice(words_list).lower()
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(0, word_length):
    placeholder += "_"
print(placeholder)

game_over = False
correct_letters = []

while not game_over:

    print(f"*****************{lives}/6 Lives Left*****************")
    guess = input("Guess a letter: ").lower()

    if guess in correct_letters:
        print(f"You have already guessed this letter: {guess}")

    display = ""


    for letter in chosen_word:
       if letter == guess:
          display += letter
          correct_letters.append(guess)
       elif letter in correct_letters:
           display += letter
       else:
          display += "_"

    print(display)

    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, that is not there in the word. You lost a life! ")
        if lives == 0:
            game_over = True
            print(f"************** It was {chosen_word}, You Lose!***************")

    if "_" not in display:
        game_over = True
        print("You win!")

    print(stages[-lives-1])
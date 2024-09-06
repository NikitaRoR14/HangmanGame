import random
import hangman_words
import hangman_art
stages = hangman_art.stages
logo = hangman_art.logo

word_list = hangman_words.word_list
chosen_word = random.choice(word_list)

print(logo)

for _ in range(3):
    print()

completion_list = []

number_of_lives = 6

game_over = False

word_progress = ""

for _ in chosen_word:
    completion_list.append("_")

for i in completion_list:
    word_progress += i

print(word_progress)

while not game_over:
    guess = input("Guess a letter: ").lower()
    if not guess in word_progress:
        if not guess in chosen_word:
            number_of_lives -= 1
            print()
            print(f"You guessed {guess}, that's not in the word. You lose a life.")
            print(f"****************************<???>/{number_of_lives} LIVES LEFT****************************")
        for letter in range(0, len(chosen_word)):
            if chosen_word[letter] == guess:
                completion_list.pop(letter)
                completion_list.insert(letter, guess)
        word_progress = ""
        for i in completion_list:
            word_progress += i
        print(word_progress)
        if number_of_lives == 0:
            game_over = True
            print()
            print()
            print(f"IT WAS {chosen_word}! YOU LOSE")
        elif word_progress == chosen_word:
            game_over = True
            print()
            print()
            print(f"IT WAS {chosen_word}! YOU WIN")
        print(stages[number_of_lives])
    else:
        print("You have already written this letter!")
print(word_progress)



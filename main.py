import random

wordlist = ['pasta', 'meatballs', 'carbonara', 'carrot', 'cheesecake', 'salmon', 'chicken', 'pork']

chosen_word = random.choice(wordlist)
used_letters = []
attempts_number = 10
#generate a word using _
guessed_word = len(chosen_word)*'_'

print("Welcome to super simple Hangman game. All words you have to guess are food names. You have only 10 lives, so don't make mistakes. Enjoy!")
while True:
    choosed_leeter = input("Please, choose one letter. ")



#swap _ with a letter when letter is in the word
    if choosed_leeter in chosen_word:
        lst = []
        for i in range(len(chosen_word)):
            if (chosen_word[i] == choosed_leeter):
                lst.append(i)
        
            for i in lst:
                guessed_word_list = list(guessed_word)

                guessed_word_list[i] = choosed_leeter
                guessed_word = "".join(guessed_word_list)

                if chosen_word == guessed_word:
                    print(guessed_word)
                    print("Congratulations and celeebrations!!! You have guessed the word!")
                    exit()




    else:
        attempts_number = attempts_number - 1
        print("You made a mistake. The number is going down, you have " + str(attempts_number) + " lives left.")

    print(guessed_word)






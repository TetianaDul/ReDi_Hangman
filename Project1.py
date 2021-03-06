import random                                                                   #Get the word that the player would have to guess

def ran_words_get():
    words_list = ['SQUIRREL', 'ELEPHANT', 'ANTELOPE', 'KANGAROO', 'BISON', 'CAMEL', 'HIPPO', 'HORSE', 'MONKEY', 'TURTLE', 'WOMBAT', 'ALPACA', 'RABBIT', 'JAGUAR']
    return random.choice(words_list)                                            #the game will be randomly choosing from the list of words

def play_game():
    word = ran_words_get()                                                       #call the random word
    correct_letters = []                                                        #creating an empty list for the letters user will guess
    incorrect_letters = []                                                           #creating an empty list for all the words that user inputed
    attempts = 8                                                                     #user has 8 attempts
    guessed = False
    mistakes = 0
    word_display = "_" * len(word)                                                    #placeholder to display a word and guessed letters in it

    #start the game
    print("Hello there! Let's play some game!")
    print('You will need to guess a word. It contains ', len(word), ' letters, and it is a name of an animal.')
    print("Word: ", word_display)
    print(stages_hangman(mistakes))
    print(word)                               #DELETE




    while guessed is False and attempts > 0:
        guess = input('Please enter a letter: ').upper()
        attempts -= 1
        if len(guess) == 1 and guess.isalpha():
            if guess in word:
                if guess in correct_letters:
                    print('You have already tried this letter. Please try again')
                    attempts += 1
                else:
                    print('You have guessed correctly! Letter '+ guess + ' is in the word)')
                    correct_letters.append(guess)
                    list_word = list(word_display)
                    indices = [i for i, letter in enumerate(word) if letter == guess]
                    for index in indices:
                        list_word[index] = guess
                    word_display = "".join(list_word)

                    if "_" not in word_display:
                        guessed = True
            elif guess not in word:
                if guess in incorrect_letters:
                    print('You have already tried this letter. Please try again')
                    attempts += 1


                else:
                 print('Letter ' + guess + ' is not in the word')
                 incorrect_letters.append(guess)
                 mistakes += 1

        else:
            print('Incorrect input. Please try again')
            attempts += 1


        print(word_display)
        print(stages_hangman(mistakes))
        print('You have ', attempts, ' tries left')
        print('\n\n')

    if guessed:
        print('You have guessed the word ', word,'! Great job, you won!')
    else:
     print('Ups, you ran out of tries, your game is over!')
     print('The word you were trying to guess is ' + word)


def stages_hangman(mistakes):
    stages = [
                """
                    --------
                    |      
                    |      
                    |     
                    |      
                    |     
                   ---
                """,

                """
                   --------
                   |      |
                   |      
                   |     
                   |      
                   |      
                  ---
                """,

                """
                   --------
                   |      |
                   |      O
                   |     
                   |      
                   |      
                  ---
                """,

                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      
                   |      
                  ---
                """,

                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                  ---
                """,

                """
                   --------
                   |      |
                   |      O
                   |     /|
                   |      |
                   |     
                  ---
                """,

                """
                   --------
                   |      |
                   |      O
                   |     /|\\
                   |      |     
                   |     
                  ---
                """,

                """
                   --------
                   |      |
                   |      0
                   |     /|\\
                   |      |
                   |     /
                  ---
                """,

                """
                   --------
                   |      |
                   |      0
                   |     /|\\
                   |      | 
                   |     /|\\ 
                  ---
                """
    ]
    return stages[mistakes]

play_game()


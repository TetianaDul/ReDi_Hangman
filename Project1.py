import random                                                                   #Get the word that the player would have to guess

def ran_words_get():
    words_list = ['SQUIRREL', 'ELEPHANT', 'ANTELOPE', 'KANGAROO', 'CAPYBARA']
    return random.choice(words_list)                                            #the game will be randomly choosing from the list of words

def play_game():
    word = ran_words_get()                                                       #call the random word
    correct_letters = []                                                        #creating an empty list for the letters user will guess
    incorrect_letters = []                                                           #creating an empty list for all the words that user inputed
    attempts = 8                                                                #user has 8 attempts
    guessed = False
    word_display = "'_'" * 8                                                    #placeholder to display a word and guessed letters in it

    #start the game
    print("Hello there! Let's play some game!")
    print("You will need to guess a word. It contains 8 letters and it is a name of an animal")
    print(word_display)
    print(word)



    while guessed is False and attempts > 0:
        guess = input('Please enter a letter: ').upper()
        print(word_display)
        attempts -= 1
        if word_display == word:
            print('You have guessed the word ', word)
            break
        if len(guess) == 1 and guess.isalpha():
            if guess in word:
                if guess in correct_letters:
                    print('You have already tried this letter. Please try again')
                    attempts += 1
                else:
                    print('You have guessed correctly! Letter '+ guess + ' is in the word)')
                    correct_letters.append(guess)
            elif guess not in word:
                if guess in incorrect_letters:
                    print('You have already tried this letter. Please try again')
                    attempts += 1
                else:
                 print('Letter ' + guess + ' is not in the word')
                 incorrect_letters.append(guess)
        else:
            print('Incorrect input. Please try again')
            attempts += 1
        print('You have ', attempts, ' tries left')

    if guessed:
        print('You have guessed the word ', word,'! Great job, you won!')
    else:
     print('Ups, you ran out of tries, your game is over!')
     print('The word you were trying to guess is ' + word)


play_game()

import random


# example:
# word = "hello"
# guesses = "aeio"
# output --> "_e__o"
def format_word(word, guesses):
    # think string building like dna to rna transcription
    # make a variable to store the output
    output = ""
    # loop through the whole word
    for i in range(len(word)):
        # if the current letter in the word is in guesses or is a space, apostrophe, or exclamation mark
        if word[i] in guesses:
            # add that letter to the output
            # output = output + word[i]
            output += word[i]
        # otherwise, add a _ to the output because it wasn't guessed
        else:
            output = output + "_"
    #return the formatted word
    return output

def game():
    # print an introduction to the game
    # TODO: optional: ask what difficulty they want and pick a word based on that below
    print("Now before we get started... chose what difficulty you would want.")
    guesses_left = 7
    optional_value = 5
    optional = input("what level between easy, hard, and medium\n")
    if optional == "easy":
         print("okay onto the easy level now")
         optional_value = 7
         guesses_left = 8
    elif optional == "medium":
        print("okay now onto the medium level")
        optional_value = 6
        guesses_left = 7
    elif optional == "hard":
        print("okay now onto the hard level")
        optional_value = 4
        guesses_left = 5
    else: 
        print("OK will go really easy...")
        optional_value = 7
        guesses_left = 10
        # INTRODUCTION TO THE GAME
    print(f"You were running late to your train!!! You have been waiting to go on this train ride for over a year, "
          f"and you just slept in a bit to much this morning... Guess the word with no more than {guesses_left} wrong guesses "
          f"to be able to get on your train ride in time!!!")
    word = pick_random_word(optional_value)
    guessed_letters = ""
    # TODO: optional: print the current ascii image representing the number of guesses left
    print(f"You have {guesses_left} wrong guesses left.")

    print(r"""                                                    _h__
                                             ___..--'  .`.
                                    ___...--'     -  .` `.`.
                           ___...--' _      -  _   .` -   `.`.
                  ___...--'  -       _   -       .`  `. - _ `.`.
           __..--'_______________ -         _  .`  _   `.   - `.`.
        .`    _ /\    -        .`      _     .`__________`. _  -`.`.
      .` -   _ /  \_     -   .`  _         .` |Train Depot|`.   - `.`.
    .`-    _  /   /\   -   .`        _   .`   |___________|  `. _   `.`.
  .`________ /__ /_ \____.`____________.`     ___       ___  - `._____`|
    |   -  __  -|    | - |  ____  |   | | _  |   |  _  |   |  _ |
    | _   |  |  | -  |   | |.--.| |___| |    |___|     |___|    |
    |     |--|  |    | _ | |'--'| |---| |   _|---|     |---|_   |
    |   - |__| _|  - |   | |.--.| |   | |    |   |_  _ |   |    |
 ---``--._      |    |   |=|'--'|=|___|=|====|___|=====|___|====|
 -- . ''  ``--._| _  |  -|_|.--.|_______|_______________________|
`--._           '--- |_  |:|'--'|:::::::|:::::::::::::::::::::::|
_____`--._ ''      . '---'``--._|:::::::|:::::::::::::::::::::::|
----------`--._          ''      ``--.._|:::::::::::::::::::::::|
`--._ _________`--._'        --     .   ''-----.................|'
     `--._----------`--._.  _           -- . :''           -    ''
          `--._ _________`--._ :'              -- . :''      -- . ''
 -- . ''       `--._ ---------`--._   -- . :''
          :'        `--._ _________`--._:'  -- . ''      -- . ''
  -- . ''     -- . ''    `--._----------`--._      -- . ''     -- . ''
                              `--._ _________`--._
 -- . ''           :'              `--._ ---------`--._-- . ''    -- . ''
          -- . ''       -- . ''         `--._ _________`--._   -- . ''
:'                 -- . ''          -- . ''  `--._----------`--._ """)

    # get the formatted word, store it in a variable
    formatted_word = format_word(word, guessed_letters)
    # TODO: print the formatted word
    print(formatted_word)
    # the game loop continues as long as the formatted word doesn't match the current word
    # and there are guesses still remaining
    # while loop is like an if statement that repeats
    while guesses_left > 0 and word != formatted_word:
        # TODO: get the user input and store it in a variable
        letter = get_single_letter_input(guessed_letters)
        # TODO:  check if the letter isn't in the word
        if letter not in word:
            # TODO: if not, subtract a guess and print how many guesses are left
            guesses_left -= 1
            print("Oh no! That letter is not in the word.\n You have " + str(guesses_left) + " guesses left!")


        # TODO: add the letter to the guessed_letters string
        guessed_letters += letter
        # TODO: update the formatted word variable
        formatted_word = format_word(word, guessed_letters)
        # TODO: optional: print the current ascii image representing the number of guesses left

        if guesses_left > 6:
            print(r"""
     o   ____          :::::::::::::::::: :::::::::::::::::: __|-----|__
     Y_,_|[]| --++++++ |[][][][][][][][]| |[][][][][][][][]| |  []M[]  |
    {|_|_|__|;|______|;|________________|;|________________|;|_________|;
     /oo--OO   oo  oo   oo oo      oo oo   oo oo      oo oo   oo     oo
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+""")

        elif guesses_left == 6:
            print(r"""     
     :::::::::::::::::: :::::::::::::::::: __|-----|__
     |[][][][][][][][]| |[][][][][][][][]| |  []6[]  |
    |________________|;|________________|;|_________|;
     oo oo      oo oo   oo oo      oo oo   oo     oo
    -+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+""")
        elif guesses_left == 5:
            print(r"""       
     :::::::: :::::::::::::::::: __|-----|__
     [][][][]| |[][][][][][][][]| |  []5[]  |
    ________|;|________________|;|_________|;
     oo oo   oo oo      oo oo   oo     oo
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+""")
        elif guesses_left == 4:
            print(r"""
:::::::::: __|-----|__
[][][][]| |  []4[]  |
__________|;|_________|;
oo oo   oo oo      oo oo
-+-+-+-+-+-+-+-+-+-+-+""")
        elif guesses_left == 3:
            print(r"""
 __|-----|__
|  []3[]  |
|_________|;
  oo     oo
+-+-+-+-+-+-+""")
        elif guesses_left == 2:
            print(r"""
_|-----|__
  []2[]  |
_________|;
 oo     oo
+-+-+-+-+-+""")
        elif guesses_left == 1:
            print(r"""
|-----|__
 []1[]  |
________|;
o     oo
-+-+-+-+-+""")
        elif guesses_left == 0:
            print(r"""
 *
 *- *  * -
 -* * -
   *- * -""")

        # TODO: print the formatted word
        print(formatted_word)

    # after the game loop is over, we need to see if they won or lost
    # TODO: if the formatted word matches the actual word, we know they won
    if formatted_word == word:
    # TODO: print a winning message
        print("CONTRATULATIONS!\n You have made it to the train station in time and are now ready to start your long awaited vacation!\n Have fun")

# TODO: otherwise, print a losing message as well as reveal what the word was
    else:
        print("OH NO! You missed the train!\n You are now devestated since the vacation which you have been waiting for has now slipped through your fingertips.\n Maybe next time.\n")
# TODO: ask if they want to play again. restart the function if they do, otherwise print an end message
    print("\nThe word we were looking for was " + word)
    print("\nYou have had a taste of how this game works,\n but there are way more words you can try to guess!! \nwould you like to try your hand again to see if you can make it to your new vacation?\n")
    question = input("Do you want to play again?????")
    if question == "yes":
        game()
    else:
        print("Have a nice day!")


def pick_random_word(difficulty):
    return random.choice(something(difficulty))

def something(difficulty):
    word = load_dictionary()
    output = []
    for i in range(len(word)):
        if word[i][0] != "X" and len(word[i]) == difficulty:
            output.append(word[i])
    return output

def load_dictionary():
    return open("./homework_05/scrabble_words.txt").read().splitlines()

def get_single_letter_input(guessed_letters):
    answer = input("You've guessed: " + guessed_letters + " so far. Enter a letter: ").upper()
    while len(answer) != 1 or answer in guessed_letters:
        answer = input("Invalid input. Please enter a single letter you haven't guessed before: ").upper()
    return answer


def get_image(guesses_left):
    images = [ ]


game()
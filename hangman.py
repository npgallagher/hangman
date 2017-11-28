#Noah G
#Hangman

        
def backstory():
    print ("You are running in a race")
    print ("Everytime you think of the wrong letter letter in your head, you accidentally trip")
    print ("You can only trip 6 times before you lose the race")
    print ("***in the interest of being family friendly, ")
    print ("no runners were hurt in the making of this game***")
def splashscreen():
    print ("                               _________             ______   ")
    print ("_______ _________ _______      ______  /_____ __________  /_  ")
    print ("__  __ `__ \  __ `/_  __ \     _  __  /_  __ `/_  ___/_  __ \\ ")
    print ("_  / / / / / /_/ /_  / / /     / /_/ / / /_/ /_(__  )_  / / / ")
    print ("/_/ /_/ /_/\__,_/ /_/ /_/      \__,_/  \__,_/ /____/ /_/ /_/  ")
    print ("                                                              ")
                                                                
def get_puzzle():
    return "kid flash"


def show_credits():
    print ("")
    print ("Thanks for playing, " + str(name))
    print ("")
    print ("This game was created and tested by Noah on 11/14/17")

def play_again():
    while True:
        decision = input("Would you like to play again? (y/n) ").lower()

        if decision == 'y' or decision == 'yes':
            return True
        elif decision == 'n' or decision == 'no':
            return False
        else:
            print("I don't understand. Please enter 'y' or 'n'.")
            
def get_solved(puzzle, guesses):
    solved = ""

    for letter in puzzle:
        if letter.isalpha():
            if letter in guesses:
                solved += letter
            else:
                solved += "-"
        else:
            solved += letter
    return solved


def get_guess():
    while True:
        letter = input("Guess a letter: ")

        if len(letter) == 1:
            if (letter).isalpha():
                return letter
            else:
                print ("You must type a single letter")
        else:
                print ("You must type a single letter")

def display_board(solved):
    print(solved)

def show_result(puzzle, solved):
    if puzzle == solved:
        print ("You win!")
        return
    else:
        print ("You lose!")
    
def play():
    puzzle = get_puzzle()
    guesses = ""
    solved = get_solved(puzzle, guesses)
    display_board(solved)

    strikes = 0
    limit = 6

    while solved != puzzle:
        letter  = get_guess()

        if letter not in puzzle:
            strikes += 1

        guesses += letter
        solved = get_solved(puzzle, guesses)
        display_board(solved)
        print ("")
        print (str(name) + "'s strikes: " + str(strikes))
        print (str(name) + "'s guesses: " + "(" + str(guesses) + ")")
        guesses += str(",")
        print ("")
        print ("")
        if strikes >= limit:
            show_result(puzzle, solved)
    show_result(puzzle, solved)
def name_cheat(name):
    if name == 'noah':
        print ("You win!!!")
    else:
        playing = True

        while playing:
            play()
            playing = play_again()
        
### game starts
splashscreen()
print ("")
backstory()
print ("")
name = input("Please type your name: ")
name_cheat(name)


show_credits()

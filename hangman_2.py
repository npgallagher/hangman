import os
import random

path = "puzzles"

file_names = os.listdir(path)

def show_splash_screen():
    x = open('splash_screen.txt', 'r')
    file_contents = x.read()
    print(file_contents)
    x.close()
    print()


show_splash_screen()





for i, f in enumerate(file_names):
    print(str(i + 1) + "), " + f[:len(f)-4])

choice = input('pick one: ')
choice = int(choice) - 1
print()

file = path + "/" + file_names[choice]
print(file)

with open(file, 'r') as f:
    lines = f.read().splitlines()

###print(lines)

category_name = lines[0]
puzzle = random.choice( lines[1:] ).lower()

print(category_name)
###print(puzzle)


        

def display_board(solved):
    print(solved)

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


def show_result(puzzle, solved):
    if puzzle == solved:
        print ("You win!")
        return
    else:
        print ("You lose!")
        

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

def play():
    guesses = ""
    solved = get_solved(puzzle, guesses)
    display_board(solved)

    strikes = 0
    limit = 6

    while solved != puzzle:
        letter = get_guess()

        if letter not in puzzle:
            strikes += 1

        guesses += letter
        solved = get_solved(puzzle, guesses)
        display_board(solved)
        print("")
        print ("strikes: " + str(strikes))
        print ("guesses: " + "(" + str(guesses) + ")")
        guesses += str(",")
        print ("")
        print ("")
        if strikes >= limit:
            show_result(puzzle, solved)
    show_result(puzzle, solved)

def show_credit_scene():
    y = open('credit_scene.txt', 'r')
    file_content = y.read()
    print(file_content)
    y.close()
    print()

play()
show_credit_scene()

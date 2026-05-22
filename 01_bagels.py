# In Bagels, a deductive logic game, you must guess a secret three-digit number based on clues. The game offers one of the following hints in response to your guess: “Pico” when your guess has a correct digit in the wrong place, “Fermi” when your guess has a correct digit in the correct place, and “Bagels” if your guess has no correct digits. You have 10 tries to guess the secret number.
import random 

def secret_number():
    '''Generate and return a string 3 digit number.'''
    num = random.randint(100, 999)
    num = str(num)
    return num

def play_again():
    play = input("Press 'P' to play again!\n" \
    ">>> ").strip().lower()
    return play

def get_clues(num, secret_num):
    hints = set()

    for i in range(3):
        if num[i] == secret_num[i]:
            hints.add("Fermi")
        elif num[i] in secret_num:
            hints.add("Pico")
    
    if len(hints) == 0:
        print("Bagels! :(")
    else:
        hints = sorted(hints)
        print(" ".join(hints))

def check_input(num):
    digits = '0123456789'
    for i in range(3):
        if (len(num) != 3) or (num[i] not in digits) :
            print("Invalid Input !!!")
            return False
    return True


def game(name="User"):
    number = secret_number()
    print(f"June >>> I am guessing a 3 digit number!! Can you guess, what is that number {name}?\n")
    guess = 0
    while guess < 10:
        guess += 1
        guessed_num = input(f"{name} >>> Guess {guess}: ")
        if not check_input(guessed_num):
            continue
        if guessed_num == number:
            print(f"{name} you have Won the game.")
            break
        else:
            get_clues(guessed_num, number)

    if guess == 10:
        print(f"'June' : The secret number was {number}.\nYou Lost the game {name}.\nBetter luck next time bro BRO.")
    else:
        print(f"Winner {name}.")
        
    if play_again() == 'p':
        game(name)
    else:
        exit


def main():
    print("Welcome to Bagels, a deductive logic game.\n")
    print("- Rules of the game.\n\n" \
          "-- You will get 10 chances to get a '3'- digit number.\n" \
          "-- The game offer one of the following hints in response to you guess.\n" \
          "-- 1)'Pico' when your guess has a correct digit in the wrong place.\n" \
          "-- 2)'Fermi' when your guess has a correct digit in the correct place.\n" \
          "-- 3)'Bagels' if your guess has no correct digits.\n"
          )
    name = input("Before starting what is your name?\nUser: ")
    print(f"Let the game begin {name}.\n")
    game(name)

if __name__ == main():
    main()


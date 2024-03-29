import random

COLOURS = ["RED", "GREEN", "BLUE", "ORANGE", "WHITE", "YELLOW"]
TRIES = 10
CODE_LENGTH = 4

def generate_code():
    code = []

    for _ in range(CODE_LENGTH):
        colour = random.choice(COLOURS)
    code.append(colour)

    return code

def guess_code():
    while True:
       guess = input("Guess: ").upper().split(" ")

       if len(guess) != CODE_LENGTH:
           print(f"You must guess {CODE_LENGTH} colours.")
           continue
       
       for colour in guess:
           if colour not in COLOURS:
               print(f"Invalid colour: {colour}. Try again.")
               break
           else:
               break
           
    return guess
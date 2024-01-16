import random

COLORS = ["RED", "GREEN", "BLUE", "ORANGE", "WHITE", "YELLOW"]
TRIES = 10
CODE_LENGTH = 4

def generate_code():
    code = []

    for _ in range(CODE_LENGTH):
        colour = random.choice(COLORS)
    code.append(colour)

    return code

def guess_code():
    guess = input("Guess: ").upper().split(" ")
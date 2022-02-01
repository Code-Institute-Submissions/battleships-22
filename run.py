from random import randint

scores = {'computer':0,'player':0}

class Board:
    """
    This class sets board size, number of ships,player name,
    board type (player or computer) and has methods for 
    adding ships and geusses and printing the board
    """
    def __init__(self, num_ships, name, type):
        self.size = size
        self.board = [["." for x in range(size)] for y in range(size)]
        self.num_ships = num_ships
        self.name = name
        self.type = type 
        self.guesses = []
        self.ships = []

    def print(self):
        for row in self.board:
            print(" ".join(row))

    def guess(self, x, y):
        self
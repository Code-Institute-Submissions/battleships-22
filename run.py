from random import randint

scores = {'computer':0,'player':0}

class Board:
    """
    This class sets board size, number of ships,player name,
    board type (player or computer) and has methods for 
    adding ships and geusses and printing the board
    """
    def __init__(self, size, num_ships, board_name, board_type):
        self.size = size
        self.board = [["." for x in range(size)] for y in range(size)]
        self.num_ships = num_ships
        self.name = board_name
        self.type = board_type 
        self.guesses = []
        self.ships = []

    def print(self):
        """
        Removes everything from the board list except the dots that make it up
        """
        for row in self.board:
            print(" ".join(row))

    def guess(self, x, y):
        """
        guesses where the ships might be
        """
        self.guesses.append((x, y))
        self.board[x][y] = "X"

        if (x, y) in self.ships:
            self.board[x][y] = "*"
            return "Hit"
        else:
            return "Miss"

    def add_ship(self, x, y, type="computer"):
        """
        adds a ship
        """
        num_ships = 4
        active = True
        while active:
            R = randint(0, 4)
            T = randint(0, 4)
            if len(self.ships) == self.num_ships:
                active = False
            else:
                self.ships.append((R, T))
                if self.type == "player":
                    self.board[R][T] = "@"
    
        
def random_point(size = 5):
    """
    Returns a random point between zero and the size
    """

user_inputs = []
print(user_inputs)

def validate_coordinates():
    """
    Checks if the coordinates are correct
    """
    active = True
    while active:
        x = input("Guess a row: \n")
        y = input("Guess a column: \n")
        try:
            xi = int(x)
            yi = int(y)
            if xi < 0 or yi < 0:
                print("Numbers must be between 0 and 4")
                continue
            elif xi > 4 or yi > 4:
                print("Numbers must be between 0 and 4")
                continue
            elif xi in user_inputs or yi in user_inputs:
                print("You cannot choose a row and column more than once")
                continue
            else:
                user_inputs.extend([xi, yi])
                print("player guessed: "+str(xi),",", str(yi))
                active = False
                return xi, yi
        except ValueError:
            print("You must enter a number between 0 and 4")
            continue



x = "lo"
y = "lm"



X = 0
Y = 0

def populate_board(board):
    """
    Adds all the elements needed to start playing the game to the board
    """
    print(board.name+"'s board:")
    board.add_ship(X, Y)
    board.print()
    
def make_guess(board):
    """
    function that lets the computer make a choice
    """

def play_game(computer_board, player_board):
    """
    Lets user play the game
    """
    g = validate_coordinates()
    cph = computer_board.guess(xi, yi)
    if cph == "Hit":
        print("player scored a hit")
    else:
        print("player missed this time")

def new_game():
    """
    Starts a new game. Sets the board size and number of ships, resets the scores and initialises the boards
    """
    size = 5
    num_ships = 4
    scores["computer"] = 0
    scores["player"] = 0
    print("\n")
    print("Welcome to battleships")
    print(f"Board size: {size}. Number of ships: {num_ships}")
    print("Top left corner is row:0 column:0")
    print("\n")
    player_name = input("Please enter your name: \n")
    print("\n")

    computer_board = Board(size, num_ships, "Computer", board_type="computer")
    player_board = Board(size, num_ships, player_name, board_type="player")

    for _ in range(1):
        populate_board(player_board)
        populate_board(computer_board)
    
    coordinates = validate_coordinates()

    play_game(computer_board, player_board)

new_game()

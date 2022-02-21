from random import randint

scores = {'computer': 0, 'player': 0}


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

user_inputs = []


def validate_coordinates():
    """
    Checks if the coordinates are correct
    """
    active = True
    while active:
        x = input("\nGuess a row: \n")
        y = input("Guess a column: \n")
        try:
            global xi
            global yi 
            xi = int(x)
            yi = int(y)
            if xi < 0 or yi < 0:
                print("Numbers must be between 0 and 4")
                continue
            elif xi > 4 or yi > 4:
                print("Numbers must be between 0 and 4")
                continue
            elif [xi, yi] in user_inputs:
                print("You cannot choose a row and column more than once")
                continue
            else:
                user_inputs.append([xi, yi])
                print("\nplayer guessed: "+str(xi), ",", str(yi))
                active = False
                return xi, yi
        except ValueError:
            print("You must enter a number between 0 and 4")
            continue


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
    global r
    global w
    r = randint(0, 4)
    w = randint(0, 4)
    return r, w


def play_game(computer_board, player_board):
    """
    Lets user play the game
    """
    cph = computer_board.guess(xi, yi)
    if cph == "Hit":
        print("player scored a hit")
        scores['player'] += 1
    else:
        print("player missed this time")

    make_guess(computer_board)
    
    print("\ncomputer guessed: "+str(r), ",", str(w))

    ph = player_board.guess(r, w)

    if ph == "Hit":
        print("computer scored a hit")
        scores['computer'] += 1
    else:
        print("computer missed this time")


def new_game():
    """
    Starts a new game. Sets the board size and number of ships, resets the
    scores and initialises the boards
    """
    size = 5
    num_ships = 4
    scores["computer"] = 0
    scores["player"] = 0
    print("\n")
    print("Welcome to battleships")
    print(f"Board size: {size}. Number of ships: {num_ships}. Rounds: 5")
    print("Top left corner is row:0 column:0")
    print("Click run program to restart game")
    print("\n")
    player_name = input("Please enter your name: \n")
    print("\n")

    computer_board = Board(size, num_ships, "Computer", board_type="computer")
    player_board = Board(size, num_ships, player_name, board_type="player")

    for _ in range(1):
        populate_board(player_board)
        populate_board(computer_board)

    running = True
    round = 1
    while running:
        coordinates = validate_coordinates()

        play_game(computer_board, player_board)

        print(f"\n{player_name}'s board:")
        player_board.print()
        print("Computer's board:")
        computer_board.print()
            
        if round == 5:
            print("\ngame has ended")
            print("The scores are:")
            print(f" Player:{scores['player']} Computer:{scores['computer']}")
            if scores['player'] > scores['computer']:
                print('You win!')
            elif scores['player'] == scores['computer']:
                print('Its a draw!')
            else:
                print('You lose better luck next time!')
            running = False
        else:
            print("\nafter this round the scores are:")
            print(f"Player:{scores['player']} Computer:{scores['computer']}")
            
        print(f"\nEnd of round {round}")

        cont = input("\nEnter n to quit or anything else to continue : \n")
        if cont == "n":
            print("\nGame has ended the scores are: ")
            print(f"Player:{scores['player']} Computer:{scores['computer']}")
            running = False

        round = round + 1

new_game()

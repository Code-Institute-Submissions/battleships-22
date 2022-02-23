import time 
from random import randint
from termcolor import colored, cprint

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

    def add_ship(self, type="computer"):
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
        x = input(colored("\nGuess a row: \n", 'green'))
        y = input(colored("Guess a column: \n", 'green'))
        try:
            global xi
            global yi 
            xi = int(x)
            yi = int(y)
            if xi < 0 or yi < 0:
                print(colored("Numbers must be between 0 and 4", 'red'))
                continue
            elif xi > 4 or yi > 4:
                print(colored("Numbers must be between 0 and 4", 'red'))
                continue
            elif [xi, yi] in user_inputs:
                long = colored("Choice must be unique", 'red')
                print(long)
                continue
            else:
                user_inputs.append([xi, yi])
                yg = "\nYour guess:"+str(xi) + ", " + str(yi)
                print(colored(yg, 'green'))
                time.sleep(0.25)
                active = False
                return xi, yi
        except ValueError:
            print(colored("You must enter a number between 0 and 4", 'red'))
            continue


def populate_board(board):
    """
    Adds all the elements needed to start playing the game to the board
    """
    print(colored(board.name+"'s board:", 'blue'))
    board.add_ship()
    board.print()
    time.sleep(0.75)


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
        print(colored('Player scored a hit!', 'green'))
        time.sleep(0.5)
        scores['player'] += 1
    else:
        print(colored('Player missed this time!', 'green'))
        time.sleep(0.5)

    make_guess(computer_board)
    
    print(colored("\ncomputer guessed: "+str(r) + "," + str(w), 'red'))
    time.sleep(0.25)

    ph = player_board.guess(r, w)

    if ph == "Hit":
        print(colored('Computer scored a hit!', 'red'))
        time.sleep(0.5)
        scores['computer'] += 1
    else:
        print(colored('Computer missed this time!', 'red'))
        time.sleep(0.5)


def start_game(player_board, computer_board, player_name):
    """
    Starts the game and lets player play for 5 rounds
    """

    populate_board(player_board)
    populate_board(computer_board)
    for index in range(5):
        print(colored("\nRound " + str(index + 1), 'yellow'))
        time.sleep(0.5)
        validate_coordinates()

        play_game(computer_board, player_board)
        pb = colored(f"\n{player_name}'s board:", 'blue')
        print(pb)
        player_board.print()
        time.sleep(1)
        cb = colored("Computer's board:", 'blue')
        print(cb)
        computer_board.print()
        time.sleep(1)
        print(colored("\nThe scores are:", 'magenta'))
        tscore = f"Player:{scores['player']} Computer:{scores['computer']}"
        print(colored(tscore, 'magenta'))
        time.sleep(1)
    
    print(colored("\ngame has ended", 'yellow'))
    if scores['player'] > scores['computer']:
        print('You win!')
    elif scores['player'] == scores['computer']:
        print(colored('Its a draw!', 'yellow'))
    else:
        print(colored('You lose better luck next time!', 'yellow'))


def new_game():
    """
    Starts a new game. Sets the board size and number of ships, resets the
    scores and initialises the boards
    """
    size = 5
    num_ships = 4
    scores["computer"] = 0
    scores["player"] = 0

    print(colored('Welcome to battleships', 'cyan', ))
    time.sleep(0.75)

    info = f"Board size: {size}. Number of ships: {num_ships}. Rounds: 5"
    game_info = colored(info, 'cyan')
    print(game_info)
    time.sleep(0.75)

    print(colored("ships may duplicate on the same row and column", 'yellow'))
    time.sleep(0.75)

    print(colored("Top left corner is row:0 column:0", 'magenta'))
    time.sleep(0.75)

    print(colored("Click run program to restart game", 'magenta'))
    time.sleep(0.75)

    print("\n")
    global player_name
    player_name = input(colored("Please enter your name: \n", 'green'))
    time.sleep(0.5)

    while len(player_name) < 2:
        print(colored("Your name must be at least 2 characters long\n", 'red'))
        player_name = input(colored("Please enter your name: \n", 'green'))
    print("\n")

    computer_board = Board(size, num_ships, "Computer", board_type="computer")
    player_board = Board(size, num_ships, player_name, board_type="player")
    
    running = True
    while running:
    
        start_game(player_board, computer_board, player_name)
        inp = "\nEnter n to quit or anything else to continue : \n"
        cont = input(colored(inp, 'green'))
        if cont == "n":
            print(colored("\nGame has ended the scores are: ", 'yellow'))
            score1 = f"Player:{scores['player']}"
            score2 = f" Computer:{scores['computer']}"
            score3 = score1+score2
            print(colored(score3, 'yellow'))
            running = False

new_game()

from pythonProject.tictactoe.game import Game
from pythonProject.tictactoe.player import Player

print("Welcome to the TicTacToe")

player1_name = input("Enter player 1 name: ")
player2_name = input("Enter player 2 name: ")

player1_sym = input(f"Enter {player1_name} symbol for the game: ")
player2_sym = input(f"Enter {player2_name} symbol for the game: ")

player1 = Player(player1_name, player1_sym)
player2 = Player(player2_name, player2_sym)

game = Game(player1, player2)


while not game.game_over():
    game.show_board()
    game.show_available_slots()

    print(f"{player1.name}'s turn: ")
    slot = int(input("Choose a slot: "))
    game.play(player1, slot)

    game.show_board()
    game.show_available_slots()

    print(f"{player2.name}'s turn: ")
    slot = int(input("Choose a slot: "))
    game.play(player2, slot)


game.announce_winner()
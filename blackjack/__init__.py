from blackjack import startBlackJack
from os import system
import table

def main():
    system('cls')
    print('Welcome to BlackJack')
    # TODO: Support multiplayer

    playerName = input("Please enter your name: ")
    game = startBlackJack(playerName)
    table_game = table.TableTurn(game)

    table_game.start()
    next_move = ''
    while not game.isGameOver():
        # Clear board here
        # Print here for choices
        next_move = input('Next move: ')
        game.getNextMove(next_move)

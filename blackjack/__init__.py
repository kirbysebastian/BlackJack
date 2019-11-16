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
    #system('cls')
    while not game.isGameOver():
        table_game.showCards()
        table_game.getBet()
        game.showChoices()
        table_game.getNextMove()
        table_game.checkRound()
        table_game.checkGame()


#TODO: Add General Logger
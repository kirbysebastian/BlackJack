#!/usr/bin/env python3

from blackjack import startBlackJack
from utils.utilities import clear
import table

def main():
    clear()
    print('Welcome to BlackJack')
    # TODO: Support multiplayer

    playerName = input("Please enter your name: ")
    game = startBlackJack(playerName)
    table_game = table.TableTurn(game)

    table_game.start()
    #clear()
    clear()
    while not game.isGameOver():
        table_game.showCards()
        table_game.getBet()
        game.showChoices()
        table_game.getNextMove()
        table_game.checkRound()
        table_game.checkGame()

if __name__ == '__main__':
	main()
#TODO: Add General Logger

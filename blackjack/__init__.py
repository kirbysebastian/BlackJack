from blackjack import startBlackJack
import table

def main():
    print('Welcome to BlackJack')
    # TODO: Support multiplayer

    playerName = input("Enter your name: ")
    game = startBlackJack(playerName)
    table_game = table.TableTurn(game)


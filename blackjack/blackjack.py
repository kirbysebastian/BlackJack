import players
import deck

def startGame():
    print('Starting BlackJack!')

    dealer = players.Player('Computer AI', 1000)
    player1 = players.Player("KP", 1000)

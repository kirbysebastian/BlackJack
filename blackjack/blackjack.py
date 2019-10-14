from os import system
import players
import deck
import random

class Blackjack():
    def __init__(self, deck, *players):
        self.numberOfPlayers = len(players)
        #print("No. of players: {}".format(len(players)))
        self.players = players
        self.is_round_over = False
        self.is_game_over = False
        self.deck = deck
        self.game_deck = deck.cardStack[:]

    def dealCards(self):
        random_card = None
        if len(self.game_deck) != 0:
            random_card = random.choice(self.game_deck)
            self.game_deck.remove(random_card)
        else:
            self.is_game_over = True
        return random_card

    def resetGameDeck(self):
        print("Deck.CardStack: {}".format(len(self.deck.cardStack)))
        #self.game_deck = self.deck.cardStack
        #print("GameDeck: {}".format(len(self.deck.cardStack)))

    def isEndOfRound(self):
        return self.is_round_over

    def isGameOver(self):
        return self.is_game_over

    def checkCardValue(self, cardFace):
        return self.deck.cards[cardFace]

def startGame(playerName):
    deck_of_cards = deck.Deck()
    dealer = players.Player('Computer AI', 100, isDealer=True)
    player1 = players.Player(playerName, 100)
    blackJack = Blackjack(deck_of_cards, dealer, player1)

    system('cls')
    # while not blackJack.isGameOver():
    #     print(blackJack.dealCards())

    #print("Size: {}".format(len(blackJack.game_deck)))
    print(blackJack.dealCards())
    #print(blackJack.dealCards())
    print("Size: {}".format(len(blackJack.game_deck)))
    blackJack.resetGameDeck()
    #print("Size: {}".format(len(blackJack.game_deck)))














# ---------------------TEST-------------------
    # print("is_Game_over: {}".format(blackJack.isEndOfRound()))

    # for cardFace in blackJack.deck.cardFace:
    #     print("\'{}\' card face has value of: {}".format(
    #         cardFace, blackJack.checkCardValue(cardFace)))

    # for player in blackJack.players:
    #     print(player, player.getBalance())
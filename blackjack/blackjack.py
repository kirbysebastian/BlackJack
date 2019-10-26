import players
import deck
import random

class Blackjack():
    def __init__(self, deck, *players):
        self.numberOfPlayers = len(players)
        self.players = players[:]
        self.is_round_over = False
        self.is_game_over = False
        self.deck = deck
        self.game_deck = deck.cardStack[:]
        self._choices = {1:'Hit', 2:'Stand'}

    def dealCards(self):
        random_card = None
        if len(self.game_deck) != 0:
            random_card = random.choice(self.game_deck)
            self.game_deck.remove(random_card)
        else:
            self.is_game_over = True
        return random_card

    def resetGameDeck(self):
        self.game_deck = self.deck.cardStack[:]

    def isEndOfRound(self):
        return self.is_round_over

    def isGameOver(self):
        return self.is_game_over

    def checkCardValue(self, cardFace):
        return self.deck.cards[cardFace]

    def showChoices(self):
        print('\n')
        for id_key, choice in self._choices.items():
            print("{} - {}".format(id_key, choice))

    def getNextMove(self, move):
        return self._choices[move]

    def next(self, next_move):
        if self._choices[next_move] == 'HIT':
            self.dealCards()


def startBlackJack(playerName):
    deck_of_cards = deck.Deck()
    dealer = players.Player('Computer AI', 100, isDealer=True)
    player1 = players.Player(playerName, 100)
    blackJack = Blackjack(deck_of_cards, dealer, player1)
    return blackJack













# ---------------------TEST-------------------
    # print("is_Game_over: {}".format(blackJack.isEndOfRound()))

    # for cardFace in blackJack.deck.cardFace:
    #     print("\'{}\' card face has value of: {}".format(
    #         cardFace, blackJack.checkCardValue(cardFace)))

    # for player in blackJack.players:
    #     print(player, player.getBalance())
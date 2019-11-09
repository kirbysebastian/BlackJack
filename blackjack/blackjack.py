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
        self._choices = {1:'HIT', 2:'STAND'}

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

    def nextMove(self, move:int):
        key_move = int(move)
        if self._choices[key_move] == 'HIT':
            pass
        elif self._choices[key_move] == 'STAND':
            pass

    def isBust(self, playerSlot):
        slot_values = [self.deck.cards[card] for card in playerSlot]
        total_value = sum(slot_values)
        return total_value > 21

    def dealer_move(self, dealer_cards):
        card_values = [self.deck.cards[card] for card in dealer_cards]
        total_card_val = sum(card_values)
        print("Dealer cards value: {}".format(total_card_val))
        if total_card_val + 10 > 21:
            return 2
        else:
            return 1



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
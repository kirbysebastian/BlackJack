from printer import Printer
from os import system

class TableTurn():
    printer = Printer()

    def __init__(self, game):
        self.round_pot = 0;
        self.is_player_bust = False # Remove for improvement
        self.is_round_start = True
        self.game = game
        self.tableSlots = {
            player:[] for player in game.players
        }
        self.receivingSlots = [p for p in self.game.players[::-1]*self.game.numberOfPlayers]

    def start(self):
        self.startFirstDeal()

    def showCards(self):
        system('cls')
        self.printer.showCards(self.tableSlots)

    def startFirstDeal(self):
        cards_dealt = []
        for deal in range(0, len(self.game.players*2)):
            cards_dealt.append(self.game.dealCards())

        #print(cards_dealt)
        for i, player in enumerate(self.receivingSlots):
            self.tableSlots[player].append(cards_dealt[i])

    def getBet(self):
        if not self.is_round_start:
            return

        bet = int(input('Bet: $')) # TODO: Create input verifier
        player = [player for player in self.game.players if not player.is_a_dealer()][0]
        if bet > player.getBalance():
            print("Insuficient Balance: ${}".format(player.getBalance()))
            self.getBet()
            return
        
        self.is_round_start = False
        player.deductMoney(bet)
        self.round_pot += bet
        print(player.getBalance())
        print("POT: {}".format(self.round_pot))

    def getNextMove(self):
        if self.is_player_bust is True:
            return

        next_move = input('Next move: ') # TODO: Create input verifier
        if next_move.isdigit() and int(next_move) in range(1,3):
            key_move = int(next_move)

            if self.game._choices[key_move] == 'HIT':
                card = self.game.dealCards()
                self.tableSlots[self.game.players[1]].append(card)
            elif self.game._choices[key_move] == 'STAND':
                self.dealerMove()

    def dealerMove(self):
        dealer_slot = [slot for player, slot in self.tableSlots.items() if player.is_a_dealer()][0]
        dealer_move = self.game.dealer_move(dealer_slot)

        self.round_pot *= 2
        if self.game._choices[dealer_move] == 'HIT':
            card = self.game.dealCards()
            self.tableSlots[self.game.players[0]].append(card)
            self.checkRound()
            return
        elif self.game._choices[dealer_move] is 'STAND':
            self.end_round()

    def end_round(self):
        self.showCards()
        self.round_winner()
        input("Enter to continue...")
        self.restartRound()

    def round_winner(self):        
        dealer_slot = [(player, slot) for player, slot in self.tableSlots.items() if player.is_a_dealer()][0]
        player_slot = [(player, slot) for player, slot in self.tableSlots.items() if not player.is_a_dealer()][0]

        dealer_cards = sum([self.game.checkCardValue(card) for card in dealer_slot[1]])
        player_cards = sum([self.game.checkCardValue(card) for card in player_slot[1]])
        print("Player total: {}".format(player_cards))
        print("Dealer total: {}".format(dealer_cards))

        if player_cards == dealer_cards:
            player_slot[0].addMoney(self.round_pot/2)
        elif player_cards > dealer_cards and player_cards <= 21:
            player_slot[0].addMoney(self.round_pot)

    def restartRound(self):
        self.clearSlots()
        self.startFirstDeal()
        self.is_round_start = True
        self.round_pot = 0
        system('cls')

    def checkRound(self):
        dealer_slot = [slot for player, slot in self.tableSlots.items() if player.is_a_dealer()][0]
        player_slot = [slot for player, slot in self.tableSlots.items() if not player.is_a_dealer()][0]

        if self.game.isBust(dealer_slot):
            self.end_round()
        elif self.game.isBust(player_slot):
            print("Player Bust!")
            self.dealerMove()

    def checkGame(self):
        for player in self.game.players:
            if not player.is_a_dealer():
                if player.getBalance() < 1:
                    self.game.is_game_over = True

    def clearSlots(self):
        players = [player for player in self.tableSlots.keys()]
        self.tableSlots = {
            player:[] for player in players
        }

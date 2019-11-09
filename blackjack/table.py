from printer import Printer

class TableTurn():
    printer = Printer()

    def __init__(self, game):
        self.game = game
        self.tableSlots = {
            player:[] for player in game.players
        }
        self.receivingSlots = [p for p in self.game.players[::-1]*self.game.numberOfPlayers]

    def start(self):
        self.startFirstDeal()
        self.printer.showCards(self.tableSlots)

    def showCards(self):
        self.printer.showCards(self.tableSlots)

    def startFirstDeal(self):
        cards_dealt = []
        for deal in range(0, len(self.game.players*2)):
            cards_dealt.append(self.game.dealCards())

        #print(cards_dealt)
        for i, player in enumerate(self.receivingSlots):
            self.tableSlots[player].append(cards_dealt[i])

    def getNextMove(self):
        next_move = input('Next move: ')

        if next_move.isdigit() and int(next_move) in range(1,3):
            key_move = int(next_move)

            if self.game._choices[key_move] == 'HIT':
                card = self.game.dealCards()
                self.tableSlots[self.game.players[1]].append(card)

            elif self.game._choices[key_move] == 'STAND':

                dealer_move = 0
                for player in self.game.players:
                    if player.is_a_dealer():
                        dealer_move = self.game.dealer_move(
                        self.tableSlots[player])

    def checkRound(self):
        # player = self.game.players[0]
        # player_slot = self.tableSlots[player]

        dealer_slot = [slot for player, slot in self.tableSlots.items() if player.is_a_dealer()]
        if self.game.isBust(dealer_slot[0]):
            self.clearSlots()
            self.startFirstDeal()

    def clearSlots(self):

        players = [player for player in self.tableSlots.keys()]

        self.tableSlots = {
            player:[] for player in players
        }
        print(self.tableSlots)


    def getNextDeal(self):
        pass
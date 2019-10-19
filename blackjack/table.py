from printer import Printer

class TableTurn():
    printer = Printer()

    def __init__(self, game):
        self.game = game
        self.tableSlots = {
            player:[] for player in game.players
        }

    def start(self):
        self.startFirstDeal()
        self.printer.showCards(self.tableSlots)

    def startFirstDeal(self):
        cards_dealt = []
        for deal in range(0, len(self.game.players*2)):
            cards_dealt.append(self.game.dealCards())

        print(cards_dealt)
        receivingSlots = [p for p in self.game.players[::-1]*self.game.numberOfPlayers]
        for i, player in enumerate(receivingSlots):
            self.tableSlots[player].append(cards_dealt[i])

    def getTableSlot(self):
        return self.tableSlots
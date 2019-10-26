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

        print(cards_dealt)        
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
                pass

    def checkRound(self):
        player = self.game.players[1]
        player_slot = self.tableSlots[player]

        if self.game.isBust(player_slot):
            self.game.is_round_over = True


    def getNextDeal(self):
        pass
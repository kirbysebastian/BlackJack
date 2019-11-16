from os import system

class Display():
    def __init__(self):
        pass

class Printer():
    def __init__(self):
        pass

    def formatDisplay(self, table_display):
        #system('cls')
        hidden_card = ''
        for player, card in table_display.items():
            dummy_card = card[:]
            if player.is_a_dealer():
                hidden_card = dummy_card[1]
                dummy_card[1] = 'HIDDEN'
                #print("hidden card: {}".format(hidden_card))

            print("{} cards: {}".format(player.name, dummy_card))

    def showCards(self, table_cards):
        table_cards = table_cards
        self.formatDisplay(table_cards)


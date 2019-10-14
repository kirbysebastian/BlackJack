
class Challenger:
    def __init__(self, name, money):
        self.name = name
        self.money = money

    def getName(self):
        return self.name

    def getBalance(self):
        return self.money

class Player(Challenger):
    def __init__(self, name, money):
        Challenger.__init__(self, name, money)

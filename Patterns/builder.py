class Burger:
    def __init__(self) -> None:
        self.buns = None
        self.patty = None
        self.cheese = None

    def setBuns(self, bunStyle):
        self.buns = bunStyle

    def setPatty(self, pattyStype):
        self.patty = pattyStype

    def setCheese(self, cheeseStyle):
        self.cheese = cheeseStyle

    def __str__(self) -> str:
        return 'Burger made of: \n{} bread \n{} patty \n{} cheese'.format(self.buns, self.patty, self.cheese)
    

class BurgetBuilder:
    def __init__(self) -> None:
        self.burger = Burger()

    def addBuns(self, bunStyle):
        self.burger.setBuns(bunStyle)
        return self

    def addPatty(self, pattyStyle):
        self.burger.setPatty(pattyStyle)
        return self
    
    def addCheese(self, cheeseStyle):
        self.burger.setCheese(cheeseStyle)
        return self

    def build(self):
        return self.burger
    

burger_builder = BurgetBuilder().build()
# \
#                                 .addBuns('Seamen') \
#                                 .addCheese('swiss cheese') \
#                                 .addPatty('vegan') \
#                                 .build()

print(burger_builder)

class Burger:
    def __init__(self, class_name, ingeridiants=[]):
        self.class_name = class_name
        self.ingerients = ingeridiants

    def print(self):
        print(self.class_name, '\ncontains: ', ', '.join([x.title() for x in self.ingerients]), '\n')

class BurgerFactory:

    def buildBurger(self, burgerName, ingeridiants):
        return Burger(burgerName, ingeridiants)
    
    def CheeseBurger(self):
        ingeridiants = ['a','b']
        return Burger("CheeseBurger", ingeridiants)
    
    def DeluxCheeseBurger(self):
        ingeridiants = ['a', 'b', 'c']
        return Burger("DeluxCheeseBurger", ingeridiants)
    
    def VeganBurger(self):
        ingeridiants = ['e', 'f', 'g', 'h']
        return Burger("VeganBurger", ingeridiants)
    
# Burgers= BurgerFactory()
# Burgers.CheeseBurger().print
# Burgers.DeluxCheeseBurger().print
# Burgers.VeganBurger().print

factory = BurgerFactory()
factory.buildBurger('Egg Burger', ['egg', 'salt', 'seamen bread', 'cheddar cheese']).print()

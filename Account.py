class Account:

    def __init__(self, name, credits=0):
        self.name = name
        self.__credits = credits

    # Metodo para adicionar creditos.
    def addCredits(self, amount):
        self.__credits += amount

    # Metodo para recuperar os creditos.
    def getCredits(self):
        print('Olá, %s. Você possui %s em conta.' % (self.name, self.__credits))

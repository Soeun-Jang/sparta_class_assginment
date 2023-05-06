class Cookie:
    def __init__(self, p):
        self.price = p

    def get_price(self):        # getter
        return self.price

    def set_price(self, int):   # setter
        self.price = int

class Cookie:
    def __init__(self):
        self.__price = 100

    @property
    def get_price(self):   #getter
        return self.__price

    @get_price.setter
    def set_price(self, int): #setter
        self.__price = int
        
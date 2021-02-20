class Auto:

    __number_of_cars = 0

    def __init__(self, farbe="rot", marke="VW", v_max=300, autohaus="Ulmer", typ="SUV"):
        self.__farbe = farbe
        self.__marke = marke
        self.__v_max = v_max
        self.__autohaus = autohaus
        self.__typ = typ

        Auto.__number_of_cars += 1


    def set_farbe(self, amount):
        self.__farbe = amount

    def set_marke(self, amount):
        self.__marke = amount

    def set_v_max(self, amount):
        self.__v_max = amount

    def set_autohaus(self, amount):
        self.__autohaus = amount

    def set_typ(self, amount):
        self.__typ = amount

    def get_typ(self):
        return self.__typ

    def __str__(self):
        return ""

    @staticmethod
    def get_number_of_cars():
        return Auto.__number_of_cars

auto1 = Auto()

print(auto1.get_typ())
print()
<<<<<<< HEAD
class Anwendungsentwickler():

    def __init__(self, name, lieblingsSprache, jahreErfahrung):
        self.__name = name
        self.__lieblingsSprache = lieblingsSprache
        self.__jahreErfahrung = jahreErfahrung
=======
class Systemintegrator():
    def __init__(self, name: str, alter: int, jahreErfahrung: int):
        self.__name = name
        self.__alter = alter
        self.__jahreErfahrung = jahreErfahrung

    def getName(self):
        return self.__name

    def getAlter(self):
        return self.__alter

    def getJahreErfahrung(self):
        return self.__alter

    def setAlter(self, alter: int):
        self.__alter = alter

    def setName(self, name: str):
        self.__name = name

    def setJahreErfahrung(self, jahreErfahrung: int):
        self.__jahreErfahrung = jahreErfahrung

    def __str__(self):
        return f'Name: {self.getName()}\nAlter: {self.getAlter()}\nErfahrung in Jahren: {self.getJahreErfahrung()}\n'
>>>>>>> 492258f94609582423138cbe0ad09de357db1b66

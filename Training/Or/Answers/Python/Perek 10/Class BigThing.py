class BigThing:
    def __init__(self, param):
        self.__param = param

    def size(self):
        if type(self.__param) == int:
            return self.__param
        elif (type(self.__param) == list) or (type(self.__param) == dict) or (type(self.__param) == str):
            return len(self.__param)

    def __str__(self):
        return f"size is {str(self.size())}"

class BigCat(BigThing):
    def __init__(self, param, mass):
        BigThing.__init__(self, param)
        self.__mass = mass
    
    def size(self):
        if self.__mass > 15:
            if self.__mass > 20:
                return "Very Fat"
            return "Fat"
        else:
            return "OK"

latif = BigCat('latif', 22)
print(latif)
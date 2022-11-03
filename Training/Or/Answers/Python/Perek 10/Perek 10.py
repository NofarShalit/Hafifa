class Dog:
    def __init__(self, name="deault name", age=0):
        self.__name = name
        self.__age = age

    def birthday(self):
        self.__age += 1

    def get_age(self):
        return self.__age
    def get_name(self):
        return self.__name
    
    def set_name(self, name):
        self.__name = name
    def set_age(self, age):
        self.__age = age
    
    def __str__(self):
        print(f"The animal is {self.get_age()} and named {self.get_name()}")

def main():
    kermit = Dog("kermit", 13)
    kermit.birthday()
    print(kermit.get_age())

if __name__ == "__main__":
    main()
class Dog:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def birthday(self):
        self.__age += 1

    def get_age(self):
        return self.__age

def main():
    kermit = Dog("kermit", 13)
    kermit.birthday()
    print(kermit.get_age())

if __name__ == "__main__":
    main()
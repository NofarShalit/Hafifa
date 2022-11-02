class Dog:
    def __init__(self, name = ''):
        self.__name = name
        self.__age = 0
    def __str__(self):
        return(f'This dog is named {self.__name} and is {self.__age} years old')
    def birthday(self):
        self.__age += 1
    def get_age(self):
        return self.__age
    def get_name(self):
        return self.__name
    def set_name(self, name):
        self.__name = name

def main():
    pass

if __name__ == '__main__':
    main()
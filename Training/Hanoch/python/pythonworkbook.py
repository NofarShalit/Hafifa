from classtoimport import Dog


class Person:
    def __init__(self, name='Ploni', age=-1):
        self.name = name
        self.age = age
        
    def say(self):
        return("Hello")
    
    def __str__(self):
        return(f"Person {self.name} is {self.age} years old")

    def get_name(self):
        return(self.name)
    
    def get_age(self):
        return(self.age)
    
    def set_name(self, name):
        self.name = name
        
    def set_age(self, age):
        self.age = age
        
class Student(Person):
    def __init__(self, name='Ploni', age=-1, avg=-1):
        Person.__init__(self, name, age)
        self.__avg = avg

    def get_avg(self):
        return(self.__avg)
    
    def set_avg(self, avg):
        self.__avg = avg    
        
        
class BigThing:
    def __init__(self, thing):
        self.thing = thing
    def size(self):
        if type(self.thing) is int:
            return self.thing
        else:
            return len(self.thing)
        
class BigCat(BigThing):
    def __init__(self, name, weight):
        BigThing.__init__(self, weight)
        self.name = name
    def size(self):
        if self.thing > 15 and self.thing <= 20:
            return 'Fat'
        elif self.thing > 20:
            return 'Very Fat'
        else:
            return 'OK'
        
def main():
    t1=BigThing(10)
    t2=BigThing("asdff")
    cat = BigCat('chips', 10)
    print(cat.size())

    
if __name__ == '__main__':
    main()
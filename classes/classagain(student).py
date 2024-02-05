class student:
    def __init__(self, name, house):
        self.__name = name
        self.__house = house
    def getName(self):
        return self.__name

p1 = student("jack", "yellow")
print(p1.getName())
# using "__" is used as a private access modifier producing an error
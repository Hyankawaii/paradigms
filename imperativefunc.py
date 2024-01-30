def Square():
    Length = float(input())
    Square = Length * Length
    return Square

def Rectangle():
    Length = float(input())
    Base = float(input())
    Rectangle = Base * Length
    return Rectangle

def Triangle():
    Base = float(input())
    Height = float(input())
    Triangle = (Base * Height) / 2
    return Triangle

def Parallelogram():
    Base = float(input())
    Height = float(input())
    Parallelogram = Base * Height
    return Parallelogram

def Circle():
    Pi = 3.14
    Radius = float(input())
    Circle = Pi * Radius * Radius
    return Circle 

def Shapes():
    Shape = str(input()) 
    if Shape == "Square" :
        Area = Square()
    elif Shape == "Rectangle" :
        Area = Rectangle()
    elif Shape == "Triangle" :
        Area = Triangle()
    elif Shape == "Parallelogram" :
        Area = Parallelogram()
    elif Shape == "Circle" :
        Area = Circle()
    print(Area)
Shapes()
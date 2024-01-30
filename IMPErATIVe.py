Shape = input()
if Shape == "Square" :
    Length =float(input())
    Square = Length * Length
    print(Square)
elif Shape == "Rectangle" :
    Length =float(input())
    Base =float(input())
    Rectangle = Base * Length
    print(Rectangle)
elif Shape == "Triangle" :
    Base =float(input())
    Height =float(input())
    Triangle = (Base * Height) / 2
    print(Triangle)
elif Shape == "Parallelogram" :
    Base =float(input())
    Height =float(input())
    Parallelogram = Base * Height
    print(Parallelogram)
elif Shape == "Circle" :
    Pi = 3.14
    Radius =float(input())
    Circle = Pi * Radius * Radius
    print(Circle) 

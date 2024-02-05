class person:
    def __init__(self, name, last):
        self.name = name
        self.Lname = last
    def printname(self):
        print(self.name, self.Lname)


class Student(person):
    
    def __init__(self, name, last, school  ):
        self.school = school 
        super().__init__(name, last) #super automatically sets the parent class# 

    
    def StudentDetails(self):
        super().printname()
        print( f"Student school: {self.school}")

class normie(person):
    pass #pass more or less inherits everything from the main/ parent class)

#sub/derived/child class can inherit all the values and methods of its parent/main class


p1 = normie("jack", "Frost")
p2 = Student("Hank", 'schneider', 'binabangsa')

p1.printname()
p2.StudentDetails()

#CLASS Person
#    PUBLIC DECLARE Name : STRING
#    PUBLIC DECLARE LName : STRING
#    PUBLIC PROCEDURE New(name : STRING, last : STRING)
#        Name <-- name
#        Lname <-- last
#    ENDPROCEDURE
#    PUBLIC PROCEDURE ShowDetails()
#        OUTPUT Name
#        OUTPUT Lname
#    ENDPROCEDURE
#ENDCLASS
#CLASS Student INHERITS Person
#    PUBLIC DECLARE School : STRING
#    PUBLIC PROCEDURE NEW(name : STRING, last : STRING, school : STRING)
#        SUPER.NEW(name, last)
#        School <-- school
#    ENDPROCEDURE
#    PUBLIC PROCEDURE Show_Student_details()
#        SUPER.ShowDetails()
#        OUTPUT School
#    ENDPROCEDURE
#CLASS Normie INHERITS Person
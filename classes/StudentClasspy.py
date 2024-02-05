class Student:
    def __init__(self, name, Class, age, house):
        self.StudentName = name
        self.StudentClass = Class
        self.StudentAge = age
        self.StudentHouse = house
    
    def StudentDetails(self):
        print( f"Student name: , {self.StudentName}")
        print( f"Student class:, {self.StudentClass}")
        print( f"Student age:,  {self.StudentAge}")
        print( f"Student house:, {self.StudentHouse}\n")

    

Student1 = Student("alex", "JC2p", 17, "Green")
Student1.StudentDetails()
Student2 = Student("john", "JC1p", 16, "Yellow")
Student2.StudentDetails()

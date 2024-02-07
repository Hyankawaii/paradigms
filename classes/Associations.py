class Salary:
     
    
    def __init__(self, Pay):
        self.MonthlyPay = Pay

    def YearlyPay(self):
        return (self.MonthlyPay * 12)



class Employee:

    def __init__(self, name , salary, bonus):
        self.Employee_Name = name
        self.Employee_Bonus = bonus
        self.Employee_Salary = salary

    def Total_Salary(self):
        return (self.Employee_Salary.YearlyPay() + self.Employee_Bonus)


class Employee2:

    def __init__(self, name , salary, bonus): #salary is a real value creates a new Salary object when run#
        self.Employee_Name = name
        self.Employee_Bonus = bonus
        self.Employee_Salary = Salary(salary)

    def Total_Salary(self):
        return (self.Employee_Salary.YearlyPay() + self.Employee_Bonus)


Sal = Salary(100)
print(Sal.YearlyPay() )
EMP1 =  Employee("potato", Sal, 10000 )
print(EMP1.Employee_Bonus, EMP1.Employee_Name, EMP1.Employee_Salary.YearlyPay())
del(EMP1)# deletes the object(EMP1)


#storing associated objects in an array#
Emp_list = [None for i in range(10)]
Emp_list[0] = Employee2("brickman", 2000, 100)
Emp_list[1] = Employee("contractor", Sal, 2000)
print(Emp_list[0].Employee_Name, Emp_list[0].Employee_Salary.YearlyPay())
print(Emp_list[1].Employee_Name, Emp_list[0].Employee_Salary.YearlyPay())
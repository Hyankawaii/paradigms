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


Sal = Salary(100)
print(Sal.YearlyPay() )
EMP1 =  Employee("potato", Sal, 10000 )
print(EMP1.Employee_Bonus, EMP1.Employee_Name, EMP1.Employee_Salary.YearlyPay())
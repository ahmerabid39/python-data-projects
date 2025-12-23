# Basic Concept:
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        print("adding a new student")
        

s1 = Student("ahmer", 90)
print(s1.name, s1.marks)

s2 = Student("ali", 80)
print(s2.name, s2.marks)


# Basic Concept:
class Car:
    clg_name = "eab_clg"

    def __init__(self, name, model):
        self.name = name
        self.model = model
        print("creating a new car")

car1 = Car("BMW", 2008)
print(car1.name, car1.model)

car2 = Car("Toyota", 2010)
print(car2.name, car2.model)


#Q1:Create student class that takes name & marks of 3 subject as arguments in constructor.
# Then create a method to print the average.    
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def avg_marks(self):
        sum = 0
        for val in self.marks:
            sum += val 
        print("hi", self.name, "your avg score is", sum/3)

std = Student("Ahmer", [80, 85, 90])
print(std.name, std.marks)
std.avg_marks()
        

#Q2:Create account with 2 attributes - balance & account no.
# create methods for debit, credit & printing the balance.
class Account:
    def __init__(self, bal, acc):
        self.balance = bal
        self.acc_no = acc

    def debit(self, amount):
        self.balance -= amount
        print("Rs.", amount, "was debited")
        print("total balance =",self.get_balance())

    def credit(self, amount):
        self.balance += amount
        print("Rs.", amount, "was credited")
        print("total balance =", self.get_balance())

    def get_balance(self):
        return self.balance
    

acc1 = Account(10000, 12345)
acc1.debit(1000)
acc1.credit(1500)

        
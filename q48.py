# Write a program to create a class Person with basic attributes such as name, age and address. Create another class Employee which is derived from Person and store information like designation, company_name, salary. Display all the information.


class Person:
    def __init__(self):
        self.name = ""
        self.age = 0
        self.address = ""

class Emplyoee(Person):
    def __init__(self):
        super().__init__()
        self.designation = ""
        self.company_name = ""
        self.salary = 0
    
    def getInfo(self):
        self.name = input("Enter name : ")
        self.age = int(input("Enter age : "))
        self.address = input("Enter address : ")
        self.designation = input("Enter designation : ")
        self.company_name = input("Enter company name : ")
        self.salary = int(input("Enter salary : "))

    def dispInfo(self):
        print(f"Name : {self.name}")
        print(f"Age : {self.age}")
        print(f"Address : {self.address}")
        print(f"Designation : {self.designation}")
        print(f"Company Name : {self.company_name}")
        print(f"Salary : {self.salary}")

obj = Emplyoee()
obj.getInfo()
obj.dispInfo()
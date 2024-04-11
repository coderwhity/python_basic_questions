# Write a program to implement composition relation.

class A:
    def printA(self):
        print("Hello World")
class B:
    def __init__(self):
        self.obj = A()
    def printB(self):
        self.obj.printA()
        print("How are you??")

ob = B()
ob.printB()
# Write a program to ask user for a number to check if it is prime or not. If user enters an alphabet or special character instead of the number, display "only numbers are allowed"

try:
    num = int(input("Enter number : "))
except Exception as e:
    print("Only numbers are allowed")
    exit()
if(num in [0,1]):
    print("Not a Prime Number")
else:
    for i in range(2,num):
        if(num%i == 0):
            print("Not a Prime number")
            exit()
    print("Prime number")
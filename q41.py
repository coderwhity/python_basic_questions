# Ask user for a number and calculate its factorial using a function

def factorial(num):
    fact = 1
    for i in range(1,num+1):
        fact*=i
    return fact
num= int(input("Enter number : "))
print(f"Factorial of {num} is {factorial(num)}")
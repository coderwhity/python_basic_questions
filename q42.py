# Write a Python module containing basic math functions such as:
# 1. average of numbers
# 2. add n numbers
# 3. square of number
# 4. cube of number
# 5. factorial of number
# Import the module in another file and demonstrate use of all functions.

from module42 import average, addNnumbers, square, cube, factorial

print("AVERAGE")
n = int(input("Enter number of elements : "))
nums = list(int(input(f"Enter {i+1} number : ")) for i in range(n))
print(f"Average is {average(nums)}")

print("ADD N NUMBERS")
n = int(input("Enter number of elements : "))
print(f"Additon is : {addNnumbers(n)}")

print("SQUARE")
n = int(input("Enter number : "))
print(f"Square of {n} is {square(n)}")

print("CUBE")
n = int(input("Enter number : "))
print(f"Cube of {n} is {cube(n)}")

print("FACTORIAL")
n = int(input("Enter number : "))
print(f"Factorial of {n} is {factorial(n)}")
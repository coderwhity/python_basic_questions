# Write a program to ask user for a number (n) and then create a list of random integers with n elements. Hint: use random module.

import random

n = int(input("Enter number : "))
rList  = []
for i in range(n):
    rList.append(random.randint(1,999))
print(f"List of random numbers : {rList}")
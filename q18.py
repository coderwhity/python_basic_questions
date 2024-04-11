# Write a program to print the table (upto 20) of any number that user enters.

num = int(input("Enter Number : "))
print(f"Table of {num}")
for i in range(1,21):
    print(f"{num} X {i} = {num*i}")
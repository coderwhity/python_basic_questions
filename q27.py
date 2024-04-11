# Write a program to print the sum of digits of an entered number

num = int(input("Enter number : "))
s = 0
for x in str(num):
    s+=int(x)
print(f"Sum of digits in number is : {s}")
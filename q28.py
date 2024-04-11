# Write a program to print the product of digits of an entered number

num = int(input("Enter number : "))
s = 1
for x in str(num):
    s*=int(x)
print(f"Sum of digits in number is : {s}")
# Write a program to deteremine if an entered number is an armstrong number or not.

num = int(input("Enter number : "))
s = 0

for x in str(num):
    s+= int(x)**len(str(num))
print(s)
if(s == num):
    print("Number is Armstrong Number.")
else:
    print("Number is not a Armstrong Number.")

# Ask user to enter a number and display if the number is positive, negative or zero.

num = int(input("Enter number : "))
if(num < 0):
    print("Number is negative.")
elif(num == 0):
    print("Number is zero")
elif(num>0):
    print("Number is positive")
else:
    print("Invalid Number")
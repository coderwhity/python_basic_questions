# Ask user to enter a number and display if it is a prme number or not

num = int(input("Enter number : "))
if(num==0):
    print("Zero is not prime nor composite.")
elif(num ==1):
    print("Not a prime number.")
else:
    for i in range(2,num):
        if(num%i == 0):
            print("Not a Prime number.")
            exit()
print("Prime Number")
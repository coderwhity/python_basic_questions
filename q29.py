# Write a program to check if the entered number is a palindrome or not.

num = int(input("Enter number : "))
revNum = int(str(num)[::-1])
if(revNum == num):
    print("Palindrome")
else:
    print("Not Palindrome")
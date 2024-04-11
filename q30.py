# Write a program with a function which returns True if the entered number is a palindrome.

def checkPalindrome(num):
    if(num==int(str(num)[::-1])):
        return True
    return False

num = int(input("Enter Number : "))
print(f"Is Palindrome : {checkPalindrome(num)}")
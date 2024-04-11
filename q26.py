# Write a program to print reverse of a number but do not use any loops.

def revNum(num):
    return int(str(num)[::-1])

num = int(input("Enter number : "))
print(f"Revered Number : {revNum(num)}")
# Write a program with a function to reverse the given number

def revNum(num):
    return (int(str(num)[::-1]))

num = int(input("Enter number : "))
print(f"Revered Number : {revNum(num)}")
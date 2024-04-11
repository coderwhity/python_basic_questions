# Write a program with a function to reverse the given number

def revNum(num):
    return (int(str(num)[::-1]))

num = int(input("Enter number : "))
print(f"Revered Number : {revNum(num)}")

# or

def revNum2(num):
    reversedNum = 0

    while num >0:
        l = num%10
        reversedNum=(reversedNum*10)+l
        num = num//10

    return reversedNum
num = int(input("Enter number : "))
print(f"Revered Number : {revNum2(num)}")
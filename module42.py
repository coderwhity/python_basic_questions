def average(nums):
    return sum(nums)/len(nums)

def addNnumbers(n):
    s = 0
    for i in range(n):
        s+= int(input(f"Enter {i+1} number : "))
    return s

def square(n):
    return n*n

def cube(n):
    return n*n*n

def factorial(n):
    s = 1
    for i in range(1,n+1):
        s*=i
    return s

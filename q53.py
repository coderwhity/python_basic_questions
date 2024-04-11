# Write a program to print Fibonacci series of n elements. Ask user to enter value of n.

n = int(input("Enter number : "))

fib_series = [0, 1] 

for i in range(2, n):
    next_num = fib_series[-1] + fib_series[-2]  
    fib_series.append(next_num)

print("Fibonacci series of", n, "elements:", fib_series)

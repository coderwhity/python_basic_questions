# Write a program with a function which returns a list of fibonacci elements.

def fibonacci(n):
    fi_series = [0,1]
    for i in range(2,n):
        new_num = fi_series[-1]+fi_series[-2]
        fi_series.append(new_num)
    return ','.join([str(x) for x in fi_series])

n = int(input("Enter number : "))
print("Fibonacci series of", n, "elements:", fibonacci(n))
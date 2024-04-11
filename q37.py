# Write a program to input a tuple of n items from the user and display the sum of all  digits of the tuple

n = int(input("Enter number of elements : "))
t = tuple(int(input(f"Enter {i+1} element : ")) for i in range(0,n))
print(t)
print(f"Sum of elements in tuple : {sum(t)}")
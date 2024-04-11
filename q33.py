# Write a program to find the largest number from a list.

numList = [234,45,25,786,234,657]
largest = 0

for number in numList:
    if number > largest:
        largest = number
print(f"Largest number from list is : {largest}")

# OR 

print(f"Largest number from list is : {max(numList)}")

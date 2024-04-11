# Write a program to sort a list in descending order

numList = [2,75,23,7,23,79]
numList1 = [2,75,23,7,23,79]

for number in numList:
    for x in range(0,len(numList)-1):
        if numList[x] < numList[x+1]:
            numList[x],numList[x+1] = numList[x+1],numList[x]
print(f"List in de3cending order : {numList}")

# OR
numList1.sort(reverse=True)
print(numList1)

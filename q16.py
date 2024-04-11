# Create a list of numbers and display every prime number from the list. If there are no prime numbers in the list, display "No prime numbers found"

lp = [234,623,73,3,20,5]
c = 0
for x in lp:
    if(x > 1):
        f = False
        for i in range(2,x):
            if(x%i==0):
                f = True
                break
        if(not f):
            c+=1
            print(f"Prime number : {x}")

if(c==0):
    print("No prime numbers found")
        
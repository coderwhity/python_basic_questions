# Write a program to print the following pattern:
# *
# ***
# *****
# ***
# *

n = -1
rm = False
while True:
    if rm == False:
        if(n <= (12//2)):
            print(n*"*")
            n+=2
        else:
            n-=2
            rm = True
    else:
        if(n==-1):
            break
        else:
            n-=2
            print(n*"*")

    
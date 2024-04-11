# Write a program to print the following pattern:
# *****
# ***
# *

c = 5
while True:
    if(c>=0):
        print(c*"*")  
        c-=2
    else:
        break

# Write a program to print the following pattern:
# *
# ***
# *****
c = 1
while True:
    if(c <= 3*2):
        print(c*"*")
        c+=2
    else:
        break
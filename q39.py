# Ask user to enter a string. Count the number of upper case, lower case letters and digits in the string and display the data.

string = input("Enter String : ")
upper = 0
lower = 0
digit = 0
for x in string:
    if(x.isupper()):
        upper+=1
    elif(x.islower()):
        lower+=1
    elif(x.isnumeric()):
        digit+=1

print(f"Loweer case : {lower}")
print(f"Upper case : {upper}")
print(f"Digits : {digit}")
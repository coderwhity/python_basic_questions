# Ask user to enter a password. Check the password for atleast:
# 1. 1 lower case alphabet
# 2. 1 upper case alphabet
# 3. 1 special character
# 4. Atleast 8 characters long

password = input("Enter password : ")
u = 0
l = 0
d = 0
s = 0
flag = False
if(len(password)>=8):
    for x in password:
        if(x.isupper()):
            u+=1
        elif(x.islower()):
            l+=1
        elif(x in "!@#$%^&*()_+-={}|[\]:;<>?~"):
            s+=1
        elif(x.isdigit):
            d+=1
    if(u==0):
        print("Atleast 1 upper case is required.")
        flag = True
    if(l==0):
        print("Atleast 1 lower case is required.")
        flag = True
    if(d==0):
        print("Atleast 1 digit is required.")
        flag = True
    if(s==0):
        print("Atleast 1 special character is required.")
        flag = True
    if(flag):
        print("Password not valid")
    else:
        print("Password is Valid")
else:
    print("Length should be greater than or equal to 8")
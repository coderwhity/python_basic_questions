# Ask user to enter a password. If the password is not 8 characters long, throw BadPasswordError.
# Note: Create user defined exception BadPasswordError.

class BadPasswordError(Exception):
    pass

try:
    password = input("Enter password : ")
    if len(password)<8:
        raise BadPasswordError("Password length should be greater then or equal to 8")
    else:
        print("Password Is Valid")
except BadPasswordError as e:
    print(e)
    
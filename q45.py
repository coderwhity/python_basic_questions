# Write a program to overload a function named as 'greet'. It must accept at most 2 and at least no parameters.
# 2 parameters namely: user's name, message to print

def greet(name=None,message=None):
    if(name != None and message != None):
        print(f"Hello {name}, {message}")
    elif(name != None and message == None):
        print(f"Hello {name}, Welcome!!!")
    elif(name == None and message != None):
        print(F"Hello, {message}")
    else:
        print("Welcome!!!")

greet()
greet(name="Prasad")
greet(message="How are you?")
greet("Prasad","Good Morning!!!")
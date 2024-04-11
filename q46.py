# Write a program with an overloaded function area() which can be used to calculate area of square and rectangle.

def area(l=None,b=None):
    if(l!=None and b!=None):
        print(f"Area of rectangle : {l*b}")
    elif(l!=None and b==None):
        print(f"Area of square : {l*l}")

area(2,3)
area(2)
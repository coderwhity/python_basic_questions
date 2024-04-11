# Write a program with an overloaded function volume() which can be used to
# calculate area of cube, cuboid and cylinder.
# Hint:
# volume of cube = (side)^3
# volume of cuboid = length * breadth * width
# volume of cylinder = PI*(radius)^2*height


def volume(length=None,breadth=None,width=None,side=None,height=None,radius =None):
    if(side!=None):
        print(f"Volume of cube is : {side**3}")
    elif(breadth!=None and width !=None and length!=None):
        print(f"Volume of cuboid is {length*breadth*width}")
    elif(height!=None and radius !=None):
        print(f"Volume of cylinder : {3.14*(radius*radius)*height}")
    else:
        print("INVALID ARGUMENTS")

volume(side=3)
volume(breadth=4,length=24,width=4)
volume(height=24,radius=6)
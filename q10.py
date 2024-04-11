# Write a program to calculate area of triangle, square and rectangle

base = float(input("Enter triangle base : "))
height = float(input("Enter triangle height : "))
aot = .5*(base*height)
print(f"Area of triangle : {aot}")

side = float(input("Enter side of square : "))
print(f"Area of square : {side*side}")

length = float(input("Enter rectangle Length : "))
breadth = float(input("Enter rectangle breadth : "))
aor = length*breadth
print(f"Area of rectangle : {aor}")
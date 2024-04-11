# Write a program to perform set operatons.

s1 = {1,2,4,6,5}
s2 = {2,34,6,3}
print(type(s1))
s1.add("Hello")
print(s1)
s1.remove(2)
print(s1)
s1.discard("Hello")
print(s1)
print(s1.pop())
print(s1)
print(s1.copy())
s1.clear()

print(s1)

# 
s1 = {1,2,4,6,5}
s2 = {2,34,6,3}

print("Union : ")
print(s1|s2)
print("Intersection : ")
print(s1 & s2)
print("Difference : ")
print(s1- s2)
print(s2-s1)
print("Symmetric Difference : ")
print(s1^s2)
print("SUBSET : ")
print(s1<=s2)
print("Is disjoint : ")
print(s1.isdisjoint(s2))
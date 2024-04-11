# Write a program to add, subtract, multiply and divide matrices.

import numpy as np

m1 = np.array([[1,2,3],[1,2,3]])
m2 = np.array([[1,2,3],[1,2,3]])

add = m1+m2
sub = m1-m2
mul = m1*m2
div = m1/m2

print(f"Addition  :\n{add}")
print(f"Subtraction  :\n{sub}")
print(f"Multiplication  :\n{mul}")
print(f"Division  :\n{div}")
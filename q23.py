# Write a program to print the following pattern:
# 1
# 12
# 123
# 1234

for i in range(1,5):
    s = ""
    for j in range(1,i+1):
        s+=str(j)
    print(s)
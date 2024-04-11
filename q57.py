# Write a program to print the number of digits in the file. For example, if the file's contents are: "1 sheep and 2 cows were sold," the output would be 2.

try:
    file_r = open('file1_57.txt','r')
    n = 0
    for x in file_r.read():
        if(x.isnumeric()):
            n+=1
    print(f"Number of digits : {n}")
except FileNotFoundError as e:
    print(e)
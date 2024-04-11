# Write a program to write data into a file. Take the data from user

try:
    data = input("Enter data : ")
    f_write = open('file1_55.txt',"w")
    f_write.write(data)
    f_write.close()

    f_read = open('file1_55.txt','r')
    print(f_read.read())
    f_read.close()
    
except FileNotFoundError as e:
    print(e)
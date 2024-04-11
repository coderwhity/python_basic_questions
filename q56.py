# Write a program to copy contents of one file

try:
    file_read = open('file1_56.txt',"r")
    file_write = open('file2_56.txt','w')
    file_write.write(file_read.read())
    file_write.close()
    file_read.close()

    file_read = open('file2_56.txt',"r")
    print(file_read.read())
    file_read.close()
except FileNotFoundError as e:
    print(e)
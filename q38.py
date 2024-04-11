# Print the entered number in words.
# For example: 1234 => One Two Three Four

numWords = {
    1:"One",
    2:"Two",
    3:"Three",
    4:"Four",
    5:"Five",
    6:"Six",
    7:"Seven",
    8:"Eight",
    9:"Nine",
    0:"Zero"
}

num = int(input("Enter number : "))
w = ""
for n in str(num):
    w += numWords[int(n)]+" "
print(w)
    
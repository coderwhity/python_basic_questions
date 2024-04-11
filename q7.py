# Write a program to find out if entered year is a leap year or not

year = int(input("Enter year : "))
if(year%4 == 0 and year%100 != 0) or (year%400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")
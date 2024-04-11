# Write a program to print calendar of the month user wants. Ask user to enter the month and year.

import calendar

year = int(input("Enter year : "))
month = int(input("Enter month : "))
print(calendar.month(year,month))
# Write a program to convert USD to INR where 1 USD = 75 INR

usd = float(input("Enter amount in USD : "))
print(f"Amount in INR : {round(75*usd,2)}")
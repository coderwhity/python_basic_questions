# Ask user for details like name, age, date of birth and save it in a dictionary

info = {}

info["name"] = input("Enter name : ")
info["age"] = int(input("Enter age :"))
info["dob"] = input("Enter Birth date : ")

print(f"Name : {info['name']}")
print(f"Age : {info['age']}")
print(f"Date Of Birth : {info['dob']}")
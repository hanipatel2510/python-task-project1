from datetime import datetime
name=str(input("Please enter your name: "))
age=int(input("Please enter your age: "))
height=float(input("Please enter your height in meters: "))
number1=int(input("Please enter your favourite number: "))
print("\nThank you ! Here is the information we collected:")
print(f"\nName: {name} (Type: {type(name)}, Memory Address: {id(name)})")
print(f"Age: {age} (Type: {type(age)}, Memory Address: {id(age)})")
print(f"Height: {height} (Type: {type(height)},  Memory Address: {id(height)})")
print(f"Favourite Number: {number1} (Type: {type(number1)},  Memory Address: {id(number1)})\n")

current_year=datetime.now().year
age=int(input("Enter your age:"))
year=int(input("Enter any past year:"))
result=current_year - age
result1=current_year-year
print(f"\nYour birth year is approximately: {result} (based on your age of {result1})")

print(f"\nThank you for using the personal Data collector. Goodbye! ")


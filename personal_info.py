# ----------------------------------------
# Name: Mohit Bhandari
# Project: Personal Information Manager
# Description: My first complete Python project
# ----------------------------------------

# Welcome message
print("=" * 45)
print("     PERSONAL INFORMATION MANAGER")
print("=" * 45)
print()

# Static information variables
name = "Mohit Bhandari"      # String variable
age = 22                  # Integer variable
city = "Delhi"            # String variable
hobby = "Gaming"          # String variable

# Ask user for input
print("Please enter your details:")
print("-" * 30)

# Favorite food input with validation
favorite_food = input("Enter your favorite food: ").strip()

while favorite_food == "":
    print("Food name cannot be empty!")
    favorite_food = input("Enter your favorite food: ").strip()

# Favorite color input with validation
favorite_color = input("Enter your favorite color: ").strip()

while favorite_color == "":
    print("Color name cannot be empty!")
    favorite_color = input("Enter your favorite color: ").strip()

# Calculate age in months
age_in_months = age * 12

# Display formatted information
print()
print("=" * 45)
print("           YOUR INFORMATION")
print("=" * 45)

print(f"Name           : {name.title()}")
print(f"Age            : {age} years")
print(f"Age in Months  : {age_in_months} months")
print(f"City           : {city.title()}")
print(f"Hobby          : {hobby.title()}")
print()

print(f"Favorite Food  : {favorite_food.title()}")
print(f"Favorite Color : {favorite_color.title()}")

print()
print("=" * 45)
print("Thank you for using the program!")
print("=" * 45)

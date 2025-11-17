# Latihan input user
userInput1 = input("Please input first name = ")
userInput2 = input("Please input last name = ")
#print(f"Your Full Name is {userInput1} {userInput2}")

# Refactoring using upper and f notation to make some outputs
fullName = f"{userInput1} {userInput2}"
print(f"Your Full Name is {fullName}")

fullName1 = f"{userInput1} {userInput2}".upper()
print(f"Your Full Name is {fullName1}")

fullName2 = f"{userInput1} {userInput2}".lower()
print(f"Your Full Name is {fullName2}")


# Alternative f notaions
print("Your Full Name is {}".format(fullName1))
print("Your Full Name is {}".format(fullName2))

# Formating ouput strings
color = input("What is your favorite color?  ")
animal = input("What is your favorite animal?  ")
print("{}, you like a {} {}!".format(fullName1,color,animal))
print("{}, you like a {} {}!".format(fullName2,color,animal))
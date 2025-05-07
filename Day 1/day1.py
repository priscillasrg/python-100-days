# # # # # # # # # # # # #
#       Printing        #
# # # # # # # # # # # # #

print("Hello Priscilla")


# # # # # # # # # # # # # # # # #
#       String manipulation     #
# # # # # # # # # # # # # # # # #

print("Hello world!"
      "\nHello world!"
      "\nHello world!")
print("\n----------")
print("Hello my name is" + " " + "Priscilla")


# # # # # # # # # # #
#       Input       #
# # # # # # # # # # #

print("Hello " + input("What is your name?") + " !")


# # # # # # # # # # # # # # #
#       Variables           #
# # # # # # # # # # # # # # #

name = "Priscilla"
print(name)

name2 = "Rosangela Maria"
print(name)

print(len(input("What is your name? ")))

username = input("What's your username?")
usernameSize = len(username)
print(usernameSize)


# # # # # # # # # # # # # # #
#       Variable Naming     #
# # # # # # # # # # # # # # #

name = "Nico"
length = len(name)
print(length)


# # # # # # # # # # # # # # # # #
#       Band Name Generator     #
# Create a greeting for your program.
# Ask the user for the city that they grew up in and store it in a variable.
# Ask the user for the name of a pet and store it in a variable.
# Combine the name of their city and pet and show them their band name.

print("Welcome to the Band Name Generator")
city = input("What's the name of the city you grew up in?\n")
petName = input("What's your pet's name?\n")
print("Your band name could be: " + city + " " + petName)
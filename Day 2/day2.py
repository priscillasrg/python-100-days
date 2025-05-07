# # # # # # # # # # # # #
#       Data types      #
# # # # # # # # # # # # #

# Subscripting
print("Hello"[0])

# String
print("123" + "345")

# Integer = Whole number
print(123 + 345)

# Large Integers
print(123_456_789)

# Float = Floating Point Number
print(3.14159)

# Boolean
print(True)
print(False)


# # # # # # # # # # # # # # # #
#       Type, Conversion      #
# # # # # # # # # # # # # # # #


print(type("Priscilla"))
print(type(111))
print(type(1.10))
print(type(True))

print(int("1") + int("2"))

text = "Number of letters in your name: "
nameUser = input("Enter your name \n")
length_of_name = len(nameUser)
convertedString = str(length_of_name)
print(text + convertedString )


# # # # # # # # # # # # # # #
#       Math Operations     #
# # # # # # # # # # # # # # #

print("My age: " + str(12))
print(123 + 100)
print(7-3)
print(3 * 2)
print(5 / 3) #return always float
print(5 // 3) #return just the rest
print( 2**3 ) #exponents

# PEMDAS
# When you have more than one operation in the same line code
# Rule: 1. ()  2. Exponents  3.Multiplication or Division  4. + or -
# The calculation start left to right


print(3 * 3 + 3 / 3 - 3) # 9 + 1 - 3 = 7

print(3 * (3 + 3) / 3 - 3) # 3


# # # # # # # # # # # # # # #
#     Number Manipulation   #
# # # # # # # # # # # # # # #


bmi = 84 / 1.65 ** 2
print(bmi)
print(int(bmi))
print(round(bmi)) # round the number (arrendondar numero)
print(round(bmi,2)) #the second digit it's when you want display only two decimal places.

score = 4
score += 1
height = 1.7
is_winning = True
print(f"Your score is =  {score}, your height is {height}.\nYou're winning is {is_winning}")

print(6 + 4 / 2 - (1 * 2))

print((int("5") / int(2.7))) #2.5


# # # # # # # # # # # # #
#     Tip Calculator    #
# # # # # # # # # # # # #

print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

percentage_tips = tip / 100
bill_and_tips = bill * percentage_tips

total = (bill + bill_and_tips) / people
final_price = round(total, 2)
print(f"Each person should pay: {final_price}")
# print("Each person should pay: " + str(round(total, 2)))

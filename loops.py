# Store the current largest number here.
# largest_number = -999999999

# # Input the first value.
# # number = int(input("Enter a number or type -1 to stop: "))

# # If the number is not equal to -1, continue.
# while number != -1:
#     # Is number larger than largest_number?
#     if number > largest_number:
#         # Yes, update largest_number.
#         largest_number = number
#     # Input the next number.
#     # number = int(input("Enter a number or type -1 to stop: "))

# # Print the largest number.
# print("The largest number is:", largest_number)

# converter, miles to kilometers and kilometers to miles

miles= 44.99
kilometers = 8999

miles_to_kilometers = miles * 1.60934
kilometers_to_miles = kilometers / 1.60934
print(miles, "miles is", round(miles_to_kilometers, 2), "kilometers")
print(kilometers, "kilometers is", round(kilometers_to_miles, 2), "miles")

#OPERATORS
x = 0
x = float(x)
y = 3 * x**3 - 2 * x**2 + 3 * x - 1
print("y =", y)

x = 1
x = float(x)
y = 3 * x**3 - 2 * x**2 + 3 * x - 1
print("y =", y)

x = -1
x = float(x)
y = 3 * x**3 - 2 * x**2 + 3 * x - 1
print("y =", y)

a= '1'
b="1"
print(a+b)

a = 6
b = 3
a /= 2 * b
print(a)

# print("String #1")
print("String #2")

print("Tell me something, user!")
anything = input()
print("Tell me something, user!", anything)

#Calculating hypotenuese

leg_a = float(input("Input first leg length: "))
leg_b = float(input("Input second leg length: "))
hypo = (leg_a**2 + leg_b**2) ** .5
print("Hypotenuse length is", hypo)

#string operators
fnam = input("May I have your first name, please? ")
lnam = input("May I have your last name, please? ")
print("Thank you.")
print("\nYour name is " + fnam + " " + lnam + ".")

print("+" + 10 * "-" + "+")
print(("|" + " " * 10 + "|\n") * 5, end="")
print("+" + 10 * "-" + "+")

x = float(input("Enter value for x: "))
y = 1./(x + 1./(x + 1./(x + 1./x)))
print("y =", y)

hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))
mins = mins + dura # find a total of all minutes
hour = hour + mins // 60 # find a number of hours hidden in minutes and update the hour
mins = mins % 60 # correct minutes to fall in the (0..59) range
hour = hour % 24 # correct hours to fall in the (0..23) range
print(hour, ":", mins, sep='')





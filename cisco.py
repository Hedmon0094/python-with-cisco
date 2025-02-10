print("Hello , world\n" * 5)

bin(5)
print(bin(5))


print("The itsy bitsy spider climbed up \n the waterspout.")
print("Down came the rain \n and washed the spider out.")
print()
print("Out came the sun \n and dried up all the rain.")

print("My name is", "Python.", end=" ")
print("Monty Python.")
print("My", "name", "is", "Monty", "Python.", sep="-")
print("My", "name", "is", sep="_", end="*")
print("Monty", "Python.", sep="*", end="*\n")
print("Programming","Essentials","in" , sep="***", end="...")
print("Python")
print("***         ***")
print("***         ***")
print("***         ***")
print("***************")
print("***************")
print("***         ***")
print("***         ***")
print("***         ***")

print("My\nname\nis\nBond.", end=" ")
print("James Bond.")

# print(fish", "chips" , sep="&"")
print("fish", "chips", sep="&")

# python literal
print("2")
print(2)

print(0o427)
# hexadecimal
x=100
print(hex(id(x)))

import hashlib
t="hedmon achacha"
value=hashlib.sha256(t.encode()).hexdigest()
print(value)

#string
print("I like \"Monty Python\"")

print("I like 'Monty Python'")
# boolean
print(True > False)
print(True < False)

print("\"I'm\"\n\"\"learning\"\"\n\"\"\"Python\"\"\"")


# python operators
# arithmetic operators
print(5 + 3)
print(5 - 3)
print(5 * 3)
print(5 / 3)
print(5 // 3)
print(5 % 3)
print(5 ** 3)
print(5 % 3)

print(2**3)
print(2**3.)
print(2.**3)
print(2.**3.)
print(2E3)
print((2 ** 4), (2 * 4.), (2 * 4))
print((-2 / 4), (2 / 4), (2 // 4), (-2 // 4))
print((2 % -4), (2 % 4), (2 ** 3 ** 2))
print(2**3**2)

# relational operators
print(5 == 5)
print(5 != 5)
print(5 > 5)
print(5 < 5)
print(5 >= 5)
print(5 <= 5)
# logical operators
x = 5
print(x > 0 and x < 10)

x = 5
print(x > 0 or x < 10)

x = 5

# comparison operators
print(5 == 5)
print(5 != 5)
print(5 > 5)
print(5 < 5)
t = int(input("Enter a number: "))
print(t > 100)

# Read two numbers
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))

# Choose the larger number
if number1 > number2:
    larger_number = number1
else:
    larger_number = number2

# Print the result
print("The larger number is:", larger_number)

# Read three numbers
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
number3 = int(input("Enter the third number: "))

# We temporarily assume that the first number
# is the largest one.
# We will verify this soon.
largest_number = number1

# We check if the second number is larger than the current largest_number
# and update the largest_number if needed.
if number2 > largest_number:
    largest_number = number2

# We check if the third number is larger than the current largest_number
# and update the largest_number if needed.
if number3 > largest_number:
    largest_number = number3

# Print the result
print("The largest number is:", largest_number)

# Read three numbers.
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
number3 = int(input("Enter the third number: "))

# Check which one of the numbers is the greatest
# and pass it to the largest_number variable.

largest_number = max(number1, number2, number3)

# Print the result.
print("The largest number is:", largest_number)

flower=str(input("Enter the flower name below:"))
if flower == "Spathiphyllum":
    print(flower + "Yes, You have got It")
elif flower == "spathiphyllum":
    print("I want a big Spathiphillum")
else:
    print("No , it is Spathiphyllum! , not" ,flower + "!" )

income = float(input("Enter the annual income: "))

if income < 85528:
	tax = income * 0.18 - 556.02
else:
	tax = (income - 85528) * 0.32 + 14839.02

if tax < 0.0:
	tax = 0.0

tax = round(tax, 0)
print("The tax is:", tax, "thalers")


year = int(input("Enter a year: "))

if year < 1582:
	print("Not within the Gregorian calendar period")
else:
	if year % 4 != 0:
		print("Common year")
	elif year % 100 != 0:
		print("Leap year")
	elif year % 400 != 0:
		print("Common year")
	else:
		print("Leap year")
  



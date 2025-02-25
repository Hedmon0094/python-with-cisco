# Question 1: Create a for loop that counts from 0 to 10, and prints odd numbers to the screen. Use the skeleton below:

for i in range(0, 11):
    if i % 2 != 0:
        print(i)
        #
        # Question 3: Create a program with a for loop and a break statement. The program should iterate over characters in an email address, exit the loop when it reaches the @ symbol, and print the part before @ on one line. Use the skeleton below:

for ch in "john.smith@pythoninstitute.org":
    if ch == "@":
        break
    print(ch, end="")

    # Question 4: Create a program with a for loop and a continue statement. The program should iterate over a string of digits, replace each 0 with x, and print the modified string to the screen. Use the skeleton below:
    for digit in "0165031806510":
     if digit == "0":
        print("x", end="")
        continue
    print(digit, end="")

    # 
    for i in range(0, 6, 3):
     print(i)
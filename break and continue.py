print("The break Instruction:")
# print("The break instruction is used to exit a loop prematurely, regardless of the loop's condition.")
for i in range(1, 6):
    if i == 3:
        break
    print(i)

print("The continue Instruction:")
# print("The continue instruction is used to skip the current block and return to the 'for' or 'while' statement.")
for i in range(1, 6):
    if i == 3:
        continue
    print(i)


    largest_number = -99999999
counter = 0

while True:
    number = int(input("Enter a number or type -1 to end the program: "))
    if number == -1:
        break
    counter += 1
    if number > largest_number:
        largest_number = number

if counter != 0:
    print("The largest number is", largest_number)
else:
    print("You haven't entered any number.")
# Design a program that uses a while loop and continuously asks the user to enter a word unless the user enters "chupacabra" as the secret exit word, in which case the message "You've successfully left the loop." should be printed to the screen, and the loop should terminate.

# Don't print any of the words entered by the user. Use the concept of conditional execution and the break statement.
while True:
    word = input("Enter a word: ")
    if word == "chupacabra":
        print("You've successfully left the loop.")
        break
# 
user_word = input("Enter a word: ")
user_word = user_word.upper()

word_without_vowels = ""

for letter in user_word:
    if letter in 'AEIOU':
        continue
    else:
        
        word_without_vowels += letter

print(word_without_vowels)

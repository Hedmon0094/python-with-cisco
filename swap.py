variable_1=10
variable_2=20
variable_3=30

variable_1, variable_2, variable_3 = variable_2, variable_3, variable_1

print(variable_1, variable_2, variable_3)

list4 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list4[0], list4[1] ,list4[2],list4[3]= list4[1], list4[0], list4[3], list4[2]
print(list4)

# Write a program that reflects these changes and lets you practice with the concept of lists. Your task is to:

# step 1: create an empty list named beatles;
# step 2: use the append() method to add the following members of the band to the list: John Lennon, Paul McCartney, and George Harrison;
# step 3: use the for loop and the append() method to prompt the user to add the following members of the band to the list: Stu Sutcliffe, and Pete Best;
# step 4: use the del instruction to remove Stu Sutcliffe and Pete Best from the list;
# step 5: use the insert() method to add Ringo Starr to the beginning of the list.

beatles = []
beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")
for i in range(2):
    beatles.append(input("Enter the name of the band member: "))
del beatles[3]
del beatles[3]
beatles.insert(0, "Ringo Starr")
print(beatles)  


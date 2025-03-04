number=[4,5,3,22,1,2,3,4,5,6,7,8,9,10]
print(len(number))
print(number)
number.append(100)
print(len(number))
print(number)

# insert() method
number=[4,5,3,22,1,2,3,4,5,6,7,8,9,10]
print(len(number))
print(number)
number.insert(2,100)
print(len(number))
print(number)
#
# # The append() method adds a new element to the end of the list.
# # The insert() method adds a new element at the specified index.

my_list = []  # Creating an empty list.

for i in range(5):
    my_list.append(i + 1)

print(my_list)

my_list = []  # Creating an empty list.

for i in range(5):
    my_list.insert(0, i + 1)

print(my_list)

# making use of the list
list1 = [1, 2, 3, 4, 5,9]  #the list is assigned a sequence of five integer values;

total = 0
for i in  range(len(list1)): #the i variable takes the values 0, 1, 2, 3, and 4, and then it indexes the list, selecting the subsequent elements: the first, second, third, fourth and fifth;

    total += list1[i] #each of these elements is added together by the += operator to the total variable, giving the final result at the end of the loop;

print(total)

# second aspect of the for loop
my_list = [10, 1, 8, 3, 5]
total = 0

for i in my_list:
    total += i

print(total)



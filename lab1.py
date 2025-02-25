# Your task is to write a program which reads the number of blocks the builders have, and outputs the height of the pyramid that can be built using these blocks.
blocks = int(input("Enter the number of blocks: "))
height=0
current_layer= 1
while blocks >= current_layer:
    height +=1
    blocks -= current_layer
    current_layer +=1
#
# Write your code here.
#	

print("The height of the pyramid:", height)

# # # Read the numbers b and h like this:
# # b = int(input())
# # h = int(input())

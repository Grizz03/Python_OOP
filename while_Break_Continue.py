# import random

# rand_num = random.randrange(1, 51)
# x = 1  # Initialize outside while loop
# while x != rand_num:
#     x += 1  # x = x + 1
# print('The random value is: ', rand_num)

# x = 1
# while x <= 20:  # checks if less than 20
#     if x % 2 == 0:  # checks for even number
#         x += 1  # adds one
#         continue  # jump back up to if statement
#     if x == 15:
#         break  # break out of loop
#     print('Odd :', x)
#     x += 1


# PINE TREE CHALLENGE ->

tree_heights = int(input('How tall is the tree: '))
spaces = tree_heights - 1
hashes = 1
stump_spaces = tree_heights - 1

while tree_heights != 0:
    for x in range(spaces):
        print(' ', end='')
    for i in range(hashes):
        print('#', end='')
    print()

    spaces -= 1
    hashes += 2
    tree_heights -= 1

for i in range(stump_spaces):
    print(' ', end='')
print('')









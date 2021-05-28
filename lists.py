import random

rand_list = ['string', 1.23, 28]  # Lists can contain multiple data types

one_to_ten = list(range(11))

rand_list = rand_list + one_to_ten

print(rand_list[0])
print('List length ', len(rand_list))
first_3 = rand_list[0:3]

for x in first_3:  # Cycle through list's index
    print('{} : {}'.format(first_3.index(x), x))  # Value i want out of there and value itself

print(first_3[0] * 3)  # grabs the 0 index of first_3 which is parent to rand_list [grabs the string]
print('string' in first_3)  # search for item in list [comes out True]
print('Index of string: ', first_3.index('string'))  # searches for item and tells the index location
print('How many string: ', first_3.count('string'))  # counts how many times the item is in list or string

first_3[0] = 'New String'  # changing value of item in list by calling index
first_3.append('Another string')  # adding item
for x in first_3:
    print('{} : {}'.format(first_3.index(x), x))


# ITERATING THROUGH LIST WITH RANDOM NUMBERS -->

num_list = []  # Create empty list
for x in range(5):  # Iterating 5 times
    num_list.append(random.randrange(1, 9))  # appending 5 random numbers to num_list
for x in num_list:  # Iterating through num_list items
    print(x)  # [5 random integers from 1 to 8]


# BUBBLE SORT SOLUTION -->
# ~ check if list[index] > list[index + 1] therefore if True swap index values ~
# -> using num_list list from above <-

i = len(num_list) - 1  # decrement for outer loop value is last Index
while i > 1:  # continue cycling until False
    j = 0
    while j < i:
        print('\nIs {} > {}'.format(num_list[j], num_list[i]))  # track comparison for values
        print()
        if num_list[j] > num_list[j + 1]:  # Creates switch of values if True
            print('Switch')
            temp = num_list[j]  # Switch values [store first part of list into temp value]
            num_list[j] = num_list[j + 1]  # new value
            num_list[j + 1] = temp  # puts value back in place
        else:
            print("Don't Switch")
        j += 1  # increase j value by 1 each iteration
        for k in num_list:  # track changes to list each iteration
            print(k, end='')
        print()
    print('End of Round')  # Show that we cycled through list 100%
    i -= 1  # decrement so list doesnt get searched over and over again
    for k in num_list:
        print(k, end='')  # output results again after decrementing
    print()










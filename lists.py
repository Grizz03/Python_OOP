rand_list = ['string', 1.23, 28]  # Lists can contain multiple data types
one_to_ten = list(range(11))
rand_list = rand_list + one_to_ten
print(rand_list[0])
print('List length ', len(rand_list))
first_3 = rand_list[0:3]

#  Cycle through list's index
for x in first_3:
    print('{} : {}'.format(first_3.index(x), x))  # Value i want out of there and value itself

print(first_3[0] * 3)  # grabs the 0 index of first_3 which is parent to rand_list [grabs the string]
print('string' in first_3)  # search for item in list [comes out True]
print('Index of string: ', first_3.index('string'))  # searches for item and tells the index location
print('How many string: ', first_3.count('string'))  # counts how many times the item is in list or string

first_3[0] = 'New String'  # changing value of item in list by calling index
first_3.append('Another string')  # adding item
for x in first_3:
    print('{} : {}'.format(first_3.index(x), x))



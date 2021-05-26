norm_string = input('Enter a string to convert to UNICODE: ')
secret_string = ''

for char in norm_string:
    secret_string += str(ord(char) - 23)  # Converts string to UNICODE
print('Secret Message: ', secret_string)
norm_string = ''

for x in range(0, len(secret_string)-1, 2):
    char_code = secret_string[x] + secret_string[x+1]
    norm_string += chr(int(char_code) + 23)  # Converts UNICODE to string

print("Original Message: ", norm_string)


# .replace([what to replace], [what to replace with])

# lstrip() strips out white space on left side

# .join() can turn list into string

# .count() can show how many times an item in in a string


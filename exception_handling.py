# while True:  # continue until break is reached.
#     try:
#         number = int(input('Please enter a number: '))
#         break  # will only break if number entered
#     except ValueError:
#         print("You didn't enter a number")
#     except:
#         print('An unknown error occurred')
#
# print('Thank you for entering a number')

# import random
#
# secret_number = random.randrange(1, 11)
#
# while True:
#     guess = int(input('Guess a number between 1 and 10: '))
#     if guess == secret_number:
#         print('You guessed the number!')
#         break

from decimal import Decimal

decimal_sum = Decimal(0)
decimal_sum += Decimal('0.01')
decimal_sum += Decimal('0.01')
decimal_sum += Decimal('0.01')
decimal_sum += Decimal('0.01')
decimal_sum += Decimal('0.03')
print('Sum = ', decimal_sum)

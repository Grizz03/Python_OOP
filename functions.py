import math


def mult_divide(num1, num2):
    return (num1 * num2), (num1 / num2)


mult, divide = mult_divide(5, 4)


# print("5 * 4 =", mult)
# print("5 / 4 =", divide)


# LIST OF PRIMES APP -->

def is_prime(num):
    for x in range(2, num):
        if num % x == 0:
            return False
    return True  # otherwise return True


def get_primes(max_number):
    list_of_primes = []
    for num1 in range(2, max_number):
        if is_prime(num1):
            list_of_primes.append(num1)
    return list_of_primes


# max_num_to_check = int(input('Search for Primes up to: '))

# list_of_primes = get_primes(max_num_to_check)
# for prime in list_of_primes:
# print(prime)


# SUM OF ALL WITH *ARGS -->

def sum_all(*args):  # -> with args you can have multiple params <-
    sum_1 = 0
    for x in args:
        sum_1 += x
    return sum_1


print('Sum: ', sum_all(1, 2, 3, 4, 5))  # input as many params as you want


# AREA OF SHAPES APP -->

def get_area(shape):
    shape = shape.lower()
    if shape == 'rectangle':
        rectangle_area()
    elif shape == 'circle':
        circle_area()
    else:
        print('Please enter rectangle or circle..')


def rectangle_area():
    length = float(input('Enter the length: '))
    width = float(input('Enter the width: '))
    area = length * width
    print('The area of the rectangle is ', area)


def circle_area():
    radius = float(input('Enter the radius: '))
    area = math.pi * (math.pow(radius, 2))
    print('the area of the circle is {:.2f}'.format(area))


def main():
    shape_type = input('Get area for what shape: ')
    get_area(shape_type)


main()

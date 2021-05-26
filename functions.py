def mult_divide(num1, num2):
    return (num1 * num2), (num1 / num2)


mult, divide = mult_divide(5, 4)

print("5 * 4 =", mult)
print("5 / 4 =", divide)


# list of primes app

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


max_num_to_check = int(input('Search for Primes up to: '))

list_of_primes = get_primes(max_num_to_check)
for prime in list_of_primes:
    print(prime)

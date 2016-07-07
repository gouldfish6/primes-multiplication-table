import sys


NUMBER_OF_PRIMES = 10


def is_prime(test_number, primes_list):
    """
    Returns True if the given number is prime and false otherwise. The primes
    list is passed for efficiency.
    """
    for prime in primes_list:
        if not test_number % prime:
            return False
    return True


def get_primes(number_of_primes):
    """
    Returns a list of primes with the length of the list being
    number_of_primes.
    """
    found_primes = 0
    primes_list = []
    test_number = 2

    while found_primes < number_of_primes:
        if is_prime(test_number, primes_list):
            primes_list.append(test_number)
            found_primes += 1
        test_number += 1

    return primes_list


def print_multiplication_table(number_list):
    """Prints a multiplication table with the numbers in number_list."""

    for number in number_list:
        sys.stdout.write('\t' + str(number))
    sys.stdout.write('\n')

    for number in number_list:
        sys.stdout.write(str(number))
        for other_number in number_list:
            sys.stdout.write('\t' + str(number*other_number) + " ")
        sys.stdout.write('\n')


primes_list = get_primes(NUMBER_OF_PRIMES)
print_multiplication_table(primes_list)

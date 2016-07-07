import unittest

import primes_multiplication_table


class TestPrimesMultiplicationTable(unittest.TestCase):
    """Tests the fuctions in primes_multiplication_table.py."""

    def test_is_prime(self):
        """
        Tests the numbers marked as prime from is_prime are actually prime and
        those that are not prime are actually composite.
        """
        test_primes_list = []
        for test_number in range(2, 100):
            is_prime = primes_multiplication_table.is_prime(
                test_number, test_primes_list)
            # Test the primes with every possible divisor
            if is_prime:
                self.assertTrue(
                    self.naive_prime_test(test_number),
                    "%d was marked as a prime but is not an actual prime." %
                    test_number)
                test_primes_list.append(test_number)
            # Test the composites to make sure there is at least one divisor
            else:
                self.assertFalse(
                    self.naive_prime_test(test_number),
                    "%d was marked as composite but is actually prime." %
                    test_number)

    def test_get_primes_length(self):
        """Tests the length of the list for get_primes is correct."""
        for number_of_primes in range(1, 100):
            primes_list = primes_multiplication_table.get_primes(
                number_of_primes)
            list_length = len(primes_list)
            self.assertEqual(list_length, number_of_primes)

    def test_get_primes_list_contains_all_prime(self):
        """
        Tests that each number in the returned list from get_primes is actually
        prime.
        """
        primes_list = primes_multiplication_table.get_primes(100)
        for prime in primes_list:
            self.assertTrue(
                self.naive_prime_test(prime),
                "%d is in the list of primes but is actualy composite." % prime)

    def naive_prime_test(self, test_number):
        """
        Tests every possible divisor to determine if the given number is prime.
        Returns True if the number is prime and False otherwise.
        """
        for number in range(2, test_number):
            if not test_number % number:
                return False
        return True


if __name__ == '__main__':
    unittest.main()

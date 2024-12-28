"""
Python implementation of the RSA encryption algorithm.

The RSA algorithm is a public-key encryption algorithm that is based on the
difficulty of factoring large integers.

"""

_memorization_prime: dict[int, bool] = {}
"""The dictionary that stores the prime numbers. 
This is used to speed up the process of finding the prime factors of a number."""
for n in (0, 1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31):
    _memorization_prime[n] = n >= 2


def is_prime(number: int) -> bool:
    """Check if a number is prime. Stores result in a dictionary to speed up the process.

    Args:
        number (unsigned long long): The number to check if it is prime.

    Returns:
        A zero of a one, representing a boolean
    """

    if number in _memorization_prime:
        return _memorization_prime[number]

    if number % 2 == 0 or number % 3 == 0:
        _memorization_prime[number] = False
        return False

    g = 5
    while g * g <= number:
        if number % g == 0 or number % (g + 2) == 0:
            _memorization_prime[number] = False
            return False
        g += 6

    _memorization_prime[number] = True
    return True


def find_prime_factors(number: int) -> set[int]:
    """Find the prime factors of a number.

    Args:
        number (int): The number to find the prime factors of.

    Returns:
        set[int]: The prime factors of the number.
    """

    if number <= 2 or is_prime(number):
        return {number}

    fac = set()
    while number % 2 == 0:
        fac.add(2)
        number >>= 1

    while number % 3 == 0:
        fac.add(3)
        number //= 3

    g = 5
    while g * g <= number:
        while number % g == 0:
            fac.add(g)
            number //= g

        while number % (g + 2) == 0:
            fac.add(g + 2)
            number //= g + 2

        g += 6

    if number > 1:
        fac.add(number)

    return fac

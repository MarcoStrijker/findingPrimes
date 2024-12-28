# cython: language_level=3str, binding=False, boundscheck=False, wraparound=False, initializedcheck=False, nonecheck=False, infer_types=False, profile=False, cdivision=False, type_version_tag=False, unraisable_tracebacks=False
# distutils: language=c++
"""
Cython implementation of the RSA encryption algorithm.

The RSA algorithm is a public-key encryption algorithm that is based on the
difficulty of factoring large integers.

"""

ctypedef unsigned long long u64

from libcpp.unordered_map cimport unordered_map


cdef unordered_map[u64, bint] _memorization_prime
"""The dictionary that stores the prime numbers"""


for i in (0, 1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31):
    _memorization_prime[i] = i >= 2



cdef bint is_prime(u64 number):
    """Check if a number is prime. Stores result in a dictionary to speed up the process.

    Args:
        number (u64): The number to check if it is prime.

    Returns:
        A zero of a one, representing a boolean
    """

    if _memorization_prime.find(number) != _memorization_prime.end():
        return _memorization_prime[number]

    if number % 2 == 0 or number % 3 == 0:
        _memorization_prime[number] = 0
        return 0

    cdef u64 g = 5
    while g * g <= number:
        if number % g == 0 or number % (g + 2) == 0:
            _memorization_prime[number] = 0
            return 0
        g += 6

    _memorization_prime[number] = 1
    return 1


cpdef set find_prime_factors(u64 number):
    if number <= 2 or is_prime(number):
        return {number}

    fac = set()
    while number % 2 == 0:
        fac.add(2)
        number >>= 1

    while number % 3 == 0:
        fac.add(3)
        number //= 3

    cdef u64 g = 5
    while g * g <= number:
        while number % g == 0:
            fac.add(g)
            number //= g

        while number % (g + 2) == 0:
            fac.add(g + 2)
            number //= (g + 2)

        g += 6

    if number > 1:
        fac.add(number)

    return fac

""" Stub file for the Cython implementation"""

from typing import Annotated, Literal

from annotated_types import Gt, Lt

bint = Literal[0, 1]
u64 = Annotated[int, Gt(0), Lt(2**64 - 1)]

def is_prime(number: u64) -> bint:
    """Checks if a number is prime.

    Args:
        number (unsigned long long): The number to check if it is prime.

    Returns:
        bool: True if the number is prime, False otherwise.
    """

def find_prime_factors(number: u64) -> set[u64]:
    """Finds the prime factors of a number.

    Args:
        number (unsigned long long): The number for which the prime factors should be found.

    Returns:
        set[unsigned long long]: The prime factors of the number.
    """

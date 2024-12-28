""" Stub file for the C implementation"""

from typing import Annotated

from annotated_types import Gt, Lt

u8 = Annotated[int, Gt(0), Lt(2**8 - 1)]
u64 = Annotated[int, Gt(0), Lt(2**64 - 1)]

def is_prime(number: u64) -> u8:
    """Checks if a number is prime.

    Args:
        number (unsigned long long): The number to check if it is prime.

    Returns:
        i8: 1 if the number is prime, 0 otherwise.
    """

def find_prime_factors(number: u64) -> set[u64]:
    """Finds the prime factors of a number.

    Args:
        number (unsigned long long): The number for which the prime factors should be found.

    Returns:
        set[unsigned long long]: The prime factors of the number.
    """

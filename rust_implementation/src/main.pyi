""" Stub file for the Rust implementation"""

from typing import Annotated

u64 = Annotated[int, 0 <= 2**64 - 1]

def is_prime(number: u64) -> bool:
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

"""

A unit test for the prime factorization implementations.

This test compares all the prime factorization implementations each other.
The test fails if the implementations do not return the same result for the same input.
"""

import random
import unittest

from python_implementation.src.main import find_prime_factors as python_implementation
from cython_implementation.src.main import find_prime_factors as cython_implementation
from c_implementation.src.main import find_prime_factors as c_implementation
from rust_implementation.src.main import find_prime_factors as rust_implementation
from mypyc_implementation.src.main import find_prime_factors as mypyc_implementation


IMPLEMENTATIONS = [
    python_implementation,
    cython_implementation,
    c_implementation,
    rust_implementation,
    mypyc_implementation,
]
""" This list determines which implementations are tested. """


class ComparisonFindPrimeFactors(unittest.TestCase):
    """
    Tests all prime factorization implementations against each other. Makes the assumption that all
    implementations are correct. The implementations are tested with fixed inputs and random inputs.

    """

    def setUp(self) -> None:
        """Checks if there are enough implementations to test."""

        if len(IMPLEMENTATIONS) <= 1:
            raise unittest.SkipTest("Not enough implementations to compare")

    def test_u32(self) -> None:
        """Test the implementations with max of 16-32 bit numbers."""

        numbers = [2**n - n for n in range(16, 33)]

        for n in numbers:
            first_result = IMPLEMENTATIONS[0](n)

            for implementation in IMPLEMENTATIONS[1:]:
                self.assertEqual(
                    implementation(n),
                    first_result,
                    f"Implementation {implementation.__name__} returned different result for {n}",
                )


    def test_random_u64	(self) -> None:
        """Test the implementations with random inputs."""

        numbers = [random.randint(2 ** 32 - 1, 2 ** 64 - 1) for _ in range(5)]

        for n in numbers:
            first_result = IMPLEMENTATIONS[0](n)

            for implementation in IMPLEMENTATIONS[1:]:
                self.assertEqual(
                    implementation(n),
                    first_result,
                    f"Implementation {implementation.__name__} returned different result for {n}",
                )


# Run the tests
class UnitFindPrimeFactors(unittest.TestCase):
    """Tests if all implementations return the correct output for fixed inputs."""

    def setUp(self) -> None:
        """
        Checks if there are any implementations to test.

        And sets up the predefined results.
        """

        if len(IMPLEMENTATIONS) == 0:
            raise unittest.SkipTest("No implementations found")

        self.predefined_results = {
            77: {11, 7},
            2381: {2381},
            45732: {2, 3, 37, 103},
            231897: {3, 17, 4547},
            32523423: {3, 1019, 10639},
            912847619: {639697, 1427},
            3423426264: {2, 3, 587, 81001},
        }

    def test_python(self) -> None:
        """Test the python implementation."""
        for number, factors in self.predefined_results.items():
            self.assertEqual(python_implementation(number), factors)

    def test_cython(self) -> None:
        """Test the cython implementation."""
        for number, factors in self.predefined_results.items():
            self.assertEqual(cython_implementation(number), factors)

    def test_rust(self) -> None:
        """Test the rust implementation."""
        for number, factors in self.predefined_results.items():
            self.assertEqual(rust_implementation(number), factors)

    def test_c(self) -> None:
        """Test the c implementation."""
        for number, factors in self.predefined_results.items():
            self.assertEqual(c_implementation(number), factors)

    def test_mypyc(self) -> None:
        """Test the mypyc implementation."""
        for number, factors in self.predefined_results.items():
            self.assertEqual(mypyc_implementation(number), factors)


if __name__ == "__main__":
    unittest.main()

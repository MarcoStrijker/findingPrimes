# breakingRSA

A multi-language implementation of prime factorization algorithms, with a focus on performance optimization. This project serves as a learning ground for different programming languages and their unique approaches to optimization.

## Overview

This project implements prime factorization algorithms in multiple languages:
- Python (baseline implementation)
- C (with Python bindings)
- Rust (with PyO3 bindings)
- Cython
- MyPyc

Each implementation follows the same algorithm but leverages language-specific optimizations. The project includes a small set of unit tests to ensure all implementations produce identical results.

## Motivation

This project was my way to get acquainted with different programming languages. The ultimate aim is to optimize finding prime factors while learning about the strengths and trade-offs of various programming languages.

## Features

- Prime factorization implementations in 5 different languages
- Automated testing suite comparing all implementations
- Memory-efficient prime number checking with memoization
- Support for 64-bit numbers
- Python bindings for all implementations

## Testing

The test suite verifies that all implementations:
- Produce identical results
- Handle edge cases correctly
- Work with numbers up to 64-bit

## License

This project is licensed under the GNU Affero General Public License v3.0 - see the LICENSE file for details.
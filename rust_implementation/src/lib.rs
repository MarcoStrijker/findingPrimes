use std::collections::HashSet;

use memoize::memoize;

use pyo3::prelude::*;


/// Check if a number is prime. Uses memoization.
///
/// # Arguments
/// * `number` - The number to check if it is prime (u64)
///
/// # Returns
/// * `bool` - True if the number is prime, False otherwise
#[memoize]
fn is_prime(number: u64) -> bool {
    if number % 2 == 0 || number % 3 == 0 {
        return false
    }

    let mut i: u64 = 5;
    while i * i <= number {
        if number % i == 0 || number % (i + 2) == 0 {
            return false;
        }
        i += 6;
    }

    return true;
}


pub fn _find_prime_factors(mut number: u64) -> HashSet<u64> {    
    // If the number itself is a prime, just return the number
    if number <= 2 || is_prime(number) {
        return HashSet::<u64>::from([number]);
    }
    
    let mut factors: HashSet<u64> = HashSet::<u64>::new();

    while number % 2 == 0 {
        factors.insert(2);
        number /= 2;
    }

    while number % 3 == 0 {
        factors.insert(3);
        number /= 3;
    }

    let mut g: u64 = 5; 
    while g * g <= number {
        while number % g == 0 {
            factors.insert(g);
            number /= g;
        }
        
        while number % (g + 2) == 0 {
            factors.insert(g + 2);
            number /= g + 2;
        }

        g += 6;
    }

    if number > 1 {
        factors.insert(number);
    }

    return factors
}


/// Memorize the low primes to speed up the process
///
/// This is done when the module is loaded
fn memorize_low_primes() {
    for i in [0, 1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31] {
        is_prime(i);
    }
}


/// Wrap the find_prime_factors
///
/// # Arguments
/// * `number` - The number to find the prime factors for
///
/// # Returns
/// * `PyResult<HashSet<u64>>` - The prime factors of the number
#[pyfunction]
fn find_prime_factors(number: u64) -> PyResult<HashSet<u64>> {
    Ok(_find_prime_factors(number))
}


/// Create a Python module with the functions
///
/// Also memorize the low primes
///
/// # Arguments
/// * `m` - The Python module
///
/// # Returns
/// * `PyResult<()>` - The Python module with the functions
#[pymodule]
#[pyo3(name = "main")]
fn main(m: &Bound<'_, PyModule>) -> PyResult<()> {
    memorize_low_primes();
    m.add_function(wrap_pyfunction!(find_prime_factors, m)?)?;
    Ok(())
}

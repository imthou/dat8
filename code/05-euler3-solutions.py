# -*- coding: utf-8 -*-
"""
  Function-oriented solution to Project Euler Problem 3
"""

import math

# Returns True if n is a multiple of n.
#   For example, is_multiple(10, 5) is True.
def is_multiple(n, m):
    return (n % m == 0)

# This is a slower method -- test all numbers up to num 
# factors(30) => [1, 2, 3, 5, 6, 10, 15, 30]
def factors_slow(num):
    return [m for m in range(1,num) if is_multiple(num, m)]

# First, finds factors up to the square root of num.
#   Then, computes the upper factors via num/n, where n is a lower-half factor
def factors(num):
    lower_factors = []
    for possible_factor in range(1, int(math.sqrt(num)) + 1):
        if is_multiple(num, possible_factor):
            lower_factors.append(possible_factor)
    
    upper_factors = \
        [int(num/factor) for factor in reversed(lower_factors) if factor**2 != num]
    
    return lower_factors + upper_factors

# Returns True if num is prime
#   (i.e. its only factors are 1 and itself)
def is_prime(num):
    return (len(factors(num)) == 2)

# Largest prime factor
def largest_prime_factor(num):
    return max(factor for factor in factors(num) if is_prime(factor))


# Project Euler Problem 3: 
#    What is the largest prime factor of 600851475143?
print(largest_prime_factor(600851475143))

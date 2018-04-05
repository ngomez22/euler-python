"""
What is the largest prime factor of the number 600851475143 ?
"""


def prime_factors(n):
    factors = []
    i = 2
    while i * i <= n:
        while n % i == 0:
            factors.append(i)
            n = n // i
        i = i + 1
    factors.append(n)
    return factors

print(prime_factors(600851475143)[-1])

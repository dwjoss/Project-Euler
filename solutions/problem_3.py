# Problem 3
# 
# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143 ?

from math import sqrt
import time

# unused for this problem, but here it is
def sieve(limit):
    """
    generate all primes less than limit
    limit: int
    """
    candidates = [True]*limit # after the algorithm concludes candidate[i] = True iff i is prime
    candidates[0] = candidates[1] = False
    res = []
    
    for i in range(2, int(sqrt(limit))):
        if candidates[i]:
            for j in range(i**2, limit, i):
                candidates[j] = False

    for num, isPrime in enumerate(candidates):
        if isPrime:
            res.append(num)

    return res

def largest_prime_factor(number):
    current = 2
    while current < number:
        if number % current == 0:
            number /= current
        else:
            current += 1
    return number

if __name__ == '__main__':
    print largest_prime_factor(600851475143)
    

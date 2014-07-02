# Problem 10
# 
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#
# Find the sum of all the primes below two million.

from math import sqrt

def sieve(limit):
    """
    generate all primes less than limit
    limit: int
    """
    candidates = [True]*limit # after the algorithm concludes candidate[i] = True iff i is prime
    candidates[0] = candidates[1] = False
    res = []
                                
    for i in range(2, int(sqrt(limit)) + 1):
        if candidates[i]:
            for j in range(i**2, limit, i):
                candidates[j] = False

    for num, isPrime in enumerate(candidates):
        if isPrime:
            res.append(num)

    return res

def prime_sum(n):
    return sum(sieve(n))

if __name__ == '__main__':
    print sieve(2000000)
    print prime_sum(2000000)

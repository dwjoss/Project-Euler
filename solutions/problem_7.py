# Problem 7 
#
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#
# What is the 10001st prime number?

from math import log, e, sqrt

def nth_prime(n):
    limit = int(n*log(n, e)) # nth prime ~ n ln(n)
    candidates = sieve(2*limit) # double the limit just to be sure the nth prime is smaller than the limit
    
    return candidates[n - 1] # n - 1 due to zero indexing in lists
   
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

if __name__ == "__main__":
    print nth_prime(10001)


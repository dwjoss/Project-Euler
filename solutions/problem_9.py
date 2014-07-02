# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
#
# a**2 + b**2 = c**2
# For example, 3**2 + 4**2 = 9 + 16 = 25 = 5**2.
#
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

from math import sqrt

def brute_force_pythagoras():
    for a in range(500):
        for b in range(500):
            c = int(sqrt(a**2 + b**2))
            if a**2 + b**2 == c**2:
                if a + b + c == 1000:
                    return a*b*c

if __name__ == '__main__':

    print brute_force_pythagoras()

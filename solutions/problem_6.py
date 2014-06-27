# The sum of the squares of the first ten natural numbers is,
#
# 1^2 + 2^2 + ... + 10^2 = 385
# 
# The square of the sum of the first ten natural numbers is,
# 
# (1 + 2 + ... + 10)^2 = 552 = 3025
# 
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 - 385 = 2640.
#
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

def square_of_sum(limit):
    return (limit*(limit + 1)/2)**2

def sum_of_squares(limit):
    return int(limit/6.0*(limit + 1)*(2*limit + 1)) # formula always returns an integer so no information loss by casting

if __name__ == "__main__":
    print square_of_sum(100) - sum_of_squares(100)


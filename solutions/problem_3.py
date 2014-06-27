# Problem 3
# 
# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143 ?

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
    

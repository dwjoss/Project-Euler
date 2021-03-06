# Problem 4
#
# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 =
# 91 x 99.
#
# Find the largest palindrome made from the product of two 3-digit numbers.
#

def brute_force_find_largest_palindrome():
    largest = 0
    for i in range(100, 1000)[::-1]:
        for j in range(100, 1000)[::-1]:
            number_string = str(i*j)
            if i*j > largest and  number_string == number_string[::-1]:
                largest = i*j
    return largest

if __name__ == "__main__":
    print brute_force_find_largest_palindrome()


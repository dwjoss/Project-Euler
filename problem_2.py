# Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:
#
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
#
# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

def generateFib(limit):
    x = 1
    y = 1
    res = [1, 1]
    
    while x + y <= limit:
        x, y = y, x + y
        res.append(y)
    
    return res

total = 0
for num in  generateFib(4000000):
    if num % 2 == 0:
        total += num
print total

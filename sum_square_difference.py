# The sum of the squares of the first ten natural numbers is,
# 12 + 22 + ... + 102 = 385
#
# The square of the sum of the first ten natural numbers is,
# (1 + 2 + ... + 10)2 = 552 = 3025
#
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.
#
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

def sum_of_squares(num):
    answer = 0
    for i in range(1, num + 1):
        answer = answer + (i*i)
    return answer

def square_of_sum(num):
    answer = 0
    for i in range(1, num + 1):
        answer = answer + i
    return(answer*answer)

answer = square_of_sum(100) - sum_of_squares(100)

print(answer)

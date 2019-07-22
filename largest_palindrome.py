# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
#
# Find the largest palindrome made from the product of two 3-digit numbers.


def is_palindrome(n):
    x = str(n)
    start = 0
    end = len(x) - 1
    while start < end:
        if x[start] is not x[end]:
            return False
        else:
            start += 1
            end -= 1
    return True


answers =[]

for i in range(100, 1000):
    for j in range(100, 1000):
        if is_palindrome(i*j):
            answers.append(i*j)

print(answers[-1])

# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143 ?


def is_prime(num):
    if num == 2:
        return True
    if num == 3:
        return True
    if num % 2 == 0:
        return False
    if num % 3 == 0:
        return False

    i = 5
    w = 2

    while i * i <= num:
        if num % i == 0:
            return False

        i += w
        w = 6 - w

    return True


def factors(num):
    factors = []
    for i in range(1, num + 1):
        print(i)
        if num % i == 0 and is_prime(i):
            factors.append(i)
    return factors


num = 600851475143

largest = factors(num)[-1]

print(largest)

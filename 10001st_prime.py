# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# 
# What is the 10 001st prime number?

primes = []
i = 1

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


while len(primes) <= 10001:
    if is_prime(i):
        primes.append(i)
    i += 1


print(primes[-1])

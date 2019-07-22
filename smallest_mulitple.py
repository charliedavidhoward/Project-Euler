# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?


def divisible(num):
    for i in range(1, 21):
        if num % i == 0:
            continue
        else:
            return False
    return True


for i in range(1, 1000000000):
    if divisible(i):
        print(i)

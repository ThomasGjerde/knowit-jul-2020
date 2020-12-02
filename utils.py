import math


def generate_primes(max):
    A = [True]*max
    A[0] = False
    A[1] = False

    for i in range(2, int(math.floor(math.sqrt(max)))):
        if A[i] is True:
            for j in range(i*i, max, i):
                A[j] = False

    primes = []
    for i in range(0, len(A)):
        if A[i] is True:
            primes.append(i)
    return primes

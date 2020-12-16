import math


def get_divisors(num):
    divisors = set()
    square_root = math.sqrt(num)
    for i in range(1, math.ceil(square_root) + 1):
        if num % i == 0:
            divisors.add(i)
            divisors.add(num//i)
    return divisors


rikelige_square = 0
for n in range(1, 1000000 + 1):
    divisors_sum = sum(get_divisors(n))
    n2 = n*2
    if divisors_sum > n2:
        divisor_n2_diff = divisors_sum - n2
        if math.ceil(math.sqrt(divisor_n2_diff)) ** 2 == divisor_n2_diff:
            rikelige_square += 1
print(rikelige_square)

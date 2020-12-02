from utils import generate_primes

gifts = 5433000
delivered = 0
primes = set(generate_primes(gifts))

gift_iter = iter(range(0, gifts + 1))
for gift_index in gift_iter:
    if '7' in str(gift_index):
        closest_lower_prime = max((x for x in primes if x <= gift_index))
        for _ in range(0, closest_lower_prime):
            next(gift_iter, None)
    else:
        delivered += 1

print(delivered)

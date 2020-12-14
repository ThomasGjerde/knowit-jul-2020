from utils import generate_primes

seq_length = 1800813
seq = [0, 1]
seq_set = set(seq)
for n in range(2, seq_length):
    subtract = seq[n-2] - n
    if subtract >= 0 and subtract not in seq_set:
        seq.append(subtract)
        seq_set.add(subtract)
    else:
        seq.append(seq[n-2] + n)
        seq_set.add(seq[n-2] + n)
primes = set(generate_primes(max(seq_set)))
prime_count = 0

for num in seq:
    if num in primes:
        prime_count += 1
print(prime_count)

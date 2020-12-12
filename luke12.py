from collections import defaultdict

relative_string = open('input/luke12.txt', 'r').read().strip()
generation_size = defaultdict(int)
current_depth = 0
for elf in relative_string.split(' '):
    current_depth += elf.count('(')
    generation_size[current_depth] += 1
    current_depth -= elf.count(')')
print(max(generation_size.items(), key=lambda x: x[1]))

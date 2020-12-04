from collections import defaultdict
ingredients = defaultdict(int)
for line in open('input/luke04.txt', 'r').readlines():
    entries = line.split(',')
    for entry in entries:
        parts = entry.split(':')
        ingredients[parts[0].strip()] += int(parts[1].strip())

print(
    min(
        ingredients['sukker'] // 2,
        ingredients['mel'] // 3,
        ingredients['melk'] // 3,
        ingredients['egg'] // 1
    )
)
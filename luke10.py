from collections import defaultdict

points = defaultdict(int)
results = [
    x.strip().split(',') for x in open('input/luke10.txt', 'r').readlines()
]

for game in results:
    for place, elf in enumerate(game, 1):
        points[elf] += len(game) - place
print(max(points.items(), key=lambda x: x[1]))

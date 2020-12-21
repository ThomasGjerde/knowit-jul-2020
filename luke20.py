from collections import defaultdict
delimiter = '🎄'

lines = open('input/luke20.txt', 'r').read().splitlines()

employed = set()
subordinates = defaultdict(set)

for line in lines:
    employed.add(line.split(delimiter)[-1])

for line in lines:
    elves = [x for x in line.split(delimiter) if x in employed]
    elves = ['Santa'] + elves
    for elf_idx, elf in enumerate(elves[:-1]):
        subordinates[elf].add(elves[elf_idx + 1])


def remove_redundant(elf):
    if not elf in subordinates.keys():
        return False
    for subordinate in list(subordinates[elf]):
        if remove_redundant(subordinate) == True:
            moved = subordinates.pop(subordinate)
            subordinates[elf].remove(subordinate)
            subordinates[elf].update(moved)
    if len(subordinates[elf]) == 1:
        if list(subordinates[elf])[0] in subordinates.keys():
            return True
        return False


remove_redundant('Santa')

workers = set()
leaders = set()
for elfs in subordinates.values():
    for elf in elfs:
        if elf not in subordinates.keys():
            workers.add(elf)
        else:
            leaders.add(elf)

print(len(workers) - len(leaders))

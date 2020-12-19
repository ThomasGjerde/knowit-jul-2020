from collections import defaultdict, deque
winners = defaultdict(int)
for line in open('input/luke19.txt', 'r').readlines():
    rule = int(line[:line.index(' ')])
    line = line[line.index(' ') + 1:]
    steps = int(line[:line.index(' ') + 1])
    elves = deque(line[line.index('[')+1:line.index(']')].split(', '))
    i = 0
    while len(elves) > 1:
        elves.rotate(steps)
        if rule == 1:
            elves.popleft()
        elif rule == 2:
            del elves[i % len(elves)]
            i = i + 1 if i <= len(elves) else 0 
        elif rule == 3:
            if len(elves) % 2 != 0:
                del elves[len(elves) // 2]
            elif len(elves) > 2:
                del elves[len(elves) // 2]
                del elves[len(elves) // 2]
            else:
                del elves[0]
        elif rule == 4:
            elves.pop()
    winners[elves[0]] += 1
print(max(winners.items(), key=lambda x: x[1]))

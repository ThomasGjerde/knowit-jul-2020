import copy


def get_neighbors(grid, pos_x, pos_y):
    len_y = len(grid)
    len_x = len(grid[0])
    neighbors = []
    for dir in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        x = pos_x + dir[1]
        y = pos_y + dir[0]
        if x > len_x - 1 or x < 0 or y > len_y - 1 or y < 0:
            continue
        neighbors.append(grid[y][x])
    return neighbors


elves = []
for line in open('input/luke09.txt', 'r').readlines():
    elves.append(list(line.strip()))

last_total_sick = None
days = 0
while last_total_sick != [x for y in elves for x in y].count('S'):
    days += 1
    last_total_sick = [x for y in elves for x in y].count('S')
    new_grid = copy.deepcopy(elves)
    for row_idx, row in enumerate(elves):
        for elf_idx, elf in enumerate(row):
            if get_neighbors(elves, elf_idx, row_idx).count('S') >= 2:
                new_grid[row_idx][elf_idx] = 'S'
    elves = new_grid
print(days)

forest = []
for line in open('input/luke07.txt', 'r').readlines():
    forest.append(list(line.rstrip('\n')))
truncs = [i for i in range(0, len(forest[-1])) if forest[-1][i] == '#']
valid = 0

for trunc_idx in truncs:
    y = len(forest) - 1
    trunc_valid = True
    while forest[y][trunc_idx] == '#' and y >= 0:
        x_offset = 0
        last_left = None
        last_right = None
        while True:
            current_left = forest[y][trunc_idx + x_offset]
            current_right = forest[y][trunc_idx - x_offset]
            if (current_right == last_right == ' ') or \
               (current_left == last_left == ' '):
               break
            if current_left != current_right:
                trunc_valid = False
                break
            last_left = current_left
            last_right = current_right
            x_offset += 1
        y -= 1
    if trunc_valid and y < len(forest) - 2 and \
       forest[y+1][trunc_idx +1] == forest[y+1][trunc_idx-1] == ' ':
        valid += 1
print(valid)
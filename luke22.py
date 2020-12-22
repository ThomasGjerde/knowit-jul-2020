from collections import defaultdict
matched = defaultdict(int)
for num, line in enumerate(open('input/luke22.txt', 'r').read().splitlines()):
    letters, names = line.split(' ', 1)
    names = names.replace('[', '').replace(']', '').split(', ')
    for name in names:
        last_index = -1
        indices = []
        temp_letters = letters
        valid = True

        for letter in list(name.lower()):
            remaining_str = temp_letters[last_index + 1:]
            if letter not in remaining_str:
                valid = False
                break
            indices.append(last_index + remaining_str.index(letter) + 1)
            last_index = indices[-1]

        if valid:
            for index in reversed(indices):
                temp_letters = temp_letters[:index] + temp_letters[index + 1:]
            letters = temp_letters
            matched[num] += 1

print(max(matched.items(), key=lambda x: x[1]))

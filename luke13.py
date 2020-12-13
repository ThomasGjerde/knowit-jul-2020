import string
input_list = list(open('input/luke13.txt', 'r').read().strip())

for letter in string.ascii_lowercase:
    indices = [i for i, x in enumerate(input_list) if x == letter]
    for idx in reversed(indices):
        if indices.index(idx) != string.ascii_lowercase.index(letter):
            del input_list[idx]
print("".join(input_list))

import string
import numpy as np
alpha = string.ascii_lowercase
password = 'eamqia'
hints = [x.strip() for x in open('input/luke11.txt', 'r').readlines()]


def generate_passwords(hint: str):
    words = []
    while len(hint) > 0:
        words.append(hint)
        hint = hint[1:]
        for i in range(0, len(hint)):
            hint = hint[:i] + \
                alpha[
                    (alpha.index(hint[i]) + 1 + alpha.index(words[-1][i])) %
                    len(alpha)] + \
                hint[i+1:]
    rectangle = [list(x) + ['']*(len(words[0])-len(x)) for x in words]
    return ["".join(x) for x in np.rot90(rectangle)]


for hint in hints:
    for candidate in generate_passwords(hint):
        if password in candidate:
            print(hint)

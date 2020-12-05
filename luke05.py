from sympy import Polygon

x = 0
y = 0
points = []

for char in open('input/luke05.txt', 'r').read():
    if char == 'O':
        y -= 1
    elif char == 'N':
        y += 1
    elif char == 'V':
        x -= 1
    elif char == 'H':
        x += 1
    else:
        raise Exception()
    points.append((y, x))
print(Polygon(*points).area)

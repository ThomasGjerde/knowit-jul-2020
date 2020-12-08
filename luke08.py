def get_distance(pos_a, pos_b):
    return abs(pos_a[0] - pos_b[0]) + \
           abs(pos_a[1] - pos_b[1])


locations = {}
time_elapsed = {}
route = []
for line in open('input/luke08.txt', 'r').readlines():
    if ':' in line:
        parts = line.strip().split(':')
        locations[parts[0]] = eval(parts[1].strip())  # Yes. I know
        time_elapsed[parts[0]] = 0.0
    else:
        route.append(line.strip())

current_pos = (0, 0)
for destination in route:
    x_dir = -1 if current_pos[0] > locations[destination][0] else 1
    y_dir = -1 if current_pos[1] > locations[destination][1] else 1
    positions = [
        (x, current_pos[1]) for x in
        range(current_pos[0] + x_dir, locations[destination][0] + x_dir, x_dir)
    ] + [
        (locations[destination][0], x) for x in
        range(current_pos[1] + y_dir, locations[destination][1] + y_dir, y_dir)
    ]

    for pos in positions:
        for location in time_elapsed.keys():
            distance = get_distance(pos, locations[location])
            if distance >= 50:
                time_elapsed[location] += 1.0
            elif distance >= 20:
                time_elapsed[location] += 0.75
            elif distance >= 5:
                time_elapsed[location] += 0.5
            elif distance >= 1:
                time_elapsed[location] += 0.25
    current_pos = locations[destination]

print(max(time_elapsed.values()) - min(time_elapsed.values()))

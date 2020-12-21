waiting_room = []
processed = 0

def process_waiting_room():
    global waiting_room
    global processed
    waiting_room = sorted(waiting_room)
    if waiting_room.pop(0)[2] == 'Claus':
        print(processed)
        exit()
    processed += 1

for i, line in enumerate(open('input/luke21.txt', 'r').read().splitlines()):
    if line == '---':
        process_waiting_room()
    else:
        waiting_room.append((int(line.split(',')[1]), i, line.split(',')[0]))

while len(waiting_room) > 0:
    process_waiting_room()

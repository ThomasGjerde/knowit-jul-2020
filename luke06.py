elves = 127
bags = [int(x) for x in open('input/luke06.txt', 'r').read().split(',')]
reversed_bags = list(reversed(bags))
all_opened = sum(bags)
for bag_id, bag in enumerate(reversed_bags):
    if (all_opened - sum(reversed_bags[:bag_id])) % elves == 0:
        print((all_opened - sum(reversed_bags[:bag_id])) // elves)
        break

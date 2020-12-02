import time
start_time = time.time()
with open('input/luke01.txt', 'r') as in_file:
    numbers = list(map(int, in_file.read().strip().split(',')))
    all_numbers = set([x for x in range(1, 100000)])
    print(all_numbers - set(numbers))
print("Completed in {}s".format((time.time() - start_time)))
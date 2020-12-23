from collections import defaultdict
base_values = {}
elf_points = defaultdict(int)
for line in open('input/luke23_words.txt', 'r').read().splitlines():
    cols = line.split(' ')
    base_values[cols[0]] = int(cols[1])
    base_values['jule' + cols[0]] = base_values[cols[0]]

for line in open('input/luke23_battle.txt', 'r').read().splitlines():
    elf = line.split(': ')[0]
    points = 0
    words = line.split(': ')[1].split(' ')
    last_vowels = None
    repition_divisor = 1
    for i, word in enumerate(words):
        val = base_values[word]
        vowels = sum([word.count(x) for x in 'aeiouyæøå'])
        if last_vowels is not None and vowels > last_vowels:
            vowel_bonus = vowels - last_vowels
            vowel_bonus *= 2 if word.startswith('jule') else 1
            val += vowel_bonus
        if i > 0 and \
           word.replace('jule', '') == words[i-1].replace('jule', ''):
            repition_divisor += 1
            val = int(val / repition_divisor)
        else:
            repition_divisor = 1
        last_vowels = vowels
        points += val
    elf_points[elf] += points
print(elf_points)

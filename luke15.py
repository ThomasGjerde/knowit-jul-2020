words = set(
    [x.strip() for x in
     open('input/luke15_wordlist.txt', 'r', encoding='utf8').readlines()])
riddles = [x.strip().split(', ') for x in
           open('input/luke15_riddles.txt', 'r', encoding='utf8').readlines()]
glue = set()
for pair in riddles:
    for word in words:
        if pair[0] + word in words and word + pair[1] in words:
            glue.add(word)

print(sum(len(x) for x in glue))

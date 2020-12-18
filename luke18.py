def is_palindrome(word):
    return word == word[::-1]

def is_palinestendrom(word):
    if len(word) <= 2:
        return False
    i = 0
    while i < (len(word) // 2) + 1:
        if word[i] == word[-(i+1)]:
            i += 1
        elif word[i] == word[-(i+2)] and word[i+1] == word[-(i+1)]:
            i += 2
        else:
            return False
    return True

num = 0
for word in open('input/luke18.txt', 'r').readlines():
    if not is_palindrome(word.strip()) and is_palinestendrom(word.strip()):
        num += 1
print(num)

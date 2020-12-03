import numpy as np

words = set()
with open('input/luke03_words.txt', 'r', encoding='utf8') as word_file:
    for line in word_file:
        words.add(line.strip())

original_matrix = []
with open('input/luke03_matrix.txt', 'r', encoding='utf8') as matrix_file:
    for line in matrix_file:
        original_matrix.append(list(line.strip()))

flipped_matrix = np.fliplr(original_matrix)
rotated_matrix = np.rot90(original_matrix)
diagonals = []
for k in range(0, len(original_matrix)):
    diagonals.append(np.diag(original_matrix, k=k))
    diagonals.append(np.diag(original_matrix, k=-k))
    diagonals.append(np.diag(flipped_matrix, k=k))
    diagonals.append(np.diag(flipped_matrix, k=-k))

found_words = set()

for matrix in [original_matrix, flipped_matrix, rotated_matrix, diagonals]:
    for row in matrix:
        row_str = "".join(row)
        row_str_reversed = "".join(reversed(row))
        for word in words - found_words:
            if word in row_str or word in row_str_reversed:
                found_words.add(word)

print(",".join(sorted(words - found_words)))

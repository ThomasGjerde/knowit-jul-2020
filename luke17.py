vacuum_str = """
  sss  
 sssss 
sssssss
sssXsss
sssssss
 sssss 
  sss  
"""
brush_str = """
kkk   kkk
kkkkkkkkk
kkkkkkkkk
 kkkkkkk 
 kkkXkkk 
 kkkkkkk 
kkkkkkkkk
kkkkkkkkk
kkk   kkk
"""


def get_positions(pos_str, char):
    matrix = []
    x = None
    for row_id, row in enumerate(pos_str.split('\n')):
        for col_id, col in enumerate(row):
            if col == char:
                matrix.append((row_id, col_id))
            elif col == 'X':
                matrix.append((row_id, col_id))
                x = (row_id, col_id)
    return [(pos[0] - x[0], pos[1] - x[1]) for pos in matrix]


vacuum_positions = get_positions(vacuum_str, 's')
brush_positions = get_positions(brush_str, 'k')
floor = {}
for row_id, row in enumerate(open('input/luke17.txt', 'r').readlines()):
    for col_id, col in enumerate(row.rstrip('\n')):
        floor[(row_id, col_id)] = col
for central_pos in floor.keys():
    valid_pos = True
    for vacuum_mod_pos in vacuum_positions:
        vacuum_pos = (central_pos[0] + vacuum_mod_pos[0],
                      central_pos[1] + vacuum_mod_pos[1])
        if vacuum_pos not in floor.keys() or floor[vacuum_pos] == 'x':
            valid_pos = False  # Overlap with edge or wall
            break

    if valid_pos:
        for brush_mod_pos in brush_positions:
            brush_pos = (central_pos[0] + brush_mod_pos[0],
                         central_pos[1] + brush_mod_pos[1])
            if brush_pos in floor.keys() and floor[brush_pos] == ' ':
                floor[brush_pos] = '.'
print(list(floor.values()).count(' '))

from ship_cargo import *
from data_arranger import *

for stack in positions:
    print(stack)

single_moves = []
single_moves = data_arrange(moves)

move_numbers = []

for move in single_moves:
    replaced = move.replace('move ', '')
    replaced_2 = replaced.replace(' from ', '')
    replaced_3 = replaced_2.replace(' to ', '')
    move_numbers.append(replaced_3)
'''
for move_stack in move_numbers:
    if len(move_stack) % 2 == 0:
        quantity = move_stack[0:2]
        place_from = int(move_stack[2])
        place_to = int(move_stack[-1])
        print(quantity + ' ' + str(place_from) + ' ' + str(place_to))
        for movement in range(int(quantity)):
            box = positions[place_from - 1].pop()
            positions[place_to - 1].append(box)
    else:
        quantity = move_stack[0]
        place_from = int(move_stack[1])
        place_to = int(move_stack[-1])
        print(quantity + ' ' + str(place_from) + ' ' + str(place_to))
        for movement in range(int(quantity)):
            box = positions[place_from - 1].pop()
            positions[place_to - 1].append(box)
'''
cycle = 0
for move_stack in move_numbers:
    boxes = 0

    if len(move_stack) % 2 == 0:
        quantity = move_stack[0:2]
        place_from = int(move_stack[2])
        place_to = int(move_stack[-1])
        print(quantity + ' ' + str(place_from) + ' ' + str(place_to))
        boxes = positions[place_from - 1][-1]
        for box in boxes:
            positions[place_to - 1].append(box)
            positions[place_from - 1].remove(box)

    else:
        quantity = move_stack[0]
        place_from = int(move_stack[1])
        place_to = int(move_stack[-1])
        print(quantity + ' ' + str(place_from) + ' ' + str(place_to))
        if quantity != '1':
            boxes = positions[place_from - 1][-(int(quantity)):]
        else:
            boxes = positions[place_from - 1][-1]
        for box in boxes:
            positions[place_to - 1].append(box)
            positions[place_from - 1].remove(box)
    cycle = cycle + 1
    for stack in positions:
        print(stack)
    print(cycle)
print(positions)
final_code = []
for pos in positions:
    final_code.append(pos[-1])

print(final_code)

from ship_cargo import *
from data_arranger import *

for stack in positions:
    print(stack)

single_moves = []
single_moves = data_arrange(moves)

move_numbers = []

for move in single_moves:
    replaced = move.replace('move ', '')
    replaced2 = replaced.replace(' from ', '')
    replaced3 = replaced2.replace(' to ', '')
    move_numbers.append(replaced3)

print(move_numbers)

for move_stack in move_numbers:
    if int(move_stack) % 2:
        quantity = move_stack[0:2]
        place_from = move_stack[2]
        place_to = move_stack[-1]
        print(quantity, place_from, place_to)
    else:
        quantity = move_stack[0]
        place_from = move_stack[1]
        place_to = move_stack[-1]
        print(quantity, place_from, place_to)

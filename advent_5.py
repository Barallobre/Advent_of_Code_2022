from ship_cargo import *
from data_arranger import *

single_moves = []
single_moves = data_arrange(moves)
move_numbers = []

for move in single_moves:
    replaced = move.replace('move ', '')
    replaced_2 = replaced.replace(' from ', '')
    replaced_3 = replaced_2.replace(' to ', '')
    move_numbers.append(replaced_3)


def first_part(move_numbers, positions_1):
    for move_stack in move_numbers:
        if len(move_stack) % 2 == 0:
            quantity = move_stack[0:2]
            place_from = int(move_stack[2])
            place_to = int(move_stack[-1])

            for movement in range(int(quantity)):
                box = positions_1[place_from - 1].pop()
                positions_1[place_to - 1].append(box)
        else:
            quantity = move_stack[0]
            place_from = int(move_stack[1])
            place_to = int(move_stack[-1])

            for movement in range(int(quantity)):
                box = positions_1[place_from - 1].pop()
                positions_1[place_to - 1].append(box)

    return positions_1


def second_part(move_numbers, positions_2):
    for move_stack in move_numbers:
        boxes = 0
        if len(move_stack) % 2 == 0:
            quantity = move_stack[0:2]
            place_from = int(move_stack[2])
            place_to = int(move_stack[-1])

            boxes = positions_2[place_from - 1][-(int(quantity)):]
            for box in boxes:
                positions_2[place_to - 1].append(box)
            for item in range(int(quantity)):
                positions_2[place_from - 1].pop()
        else:
            quantity = move_stack[0]
            place_from = int(move_stack[1])
            place_to = int(move_stack[-1])

            if quantity != '1':
                boxes = positions_2[place_from - 1][-(int(quantity)):]
            else:
                boxes = positions_2[place_from - 1][-1]
            for box in boxes:
                positions_2[place_to - 1].append(box)
            for item in range(int(quantity)):
                positions_2[place_from - 1].pop()

    return positions_2


def solved_output(copied_positions):
    final_code = ''
    for pos in copied_positions:
        final_code = final_code + pos[-1]
    print(final_code)


crate_positions_1 = []
crate_positions_2 = []
crate_positions_1 = [row[:] for row in positions]
crate_positions_2 = [row[:] for row in positions]

copied_positions = first_part(move_numbers, crate_positions_1)
solved_output(copied_positions)
copied_positions = second_part(move_numbers, crate_positions_2)
solved_output(copied_positions)

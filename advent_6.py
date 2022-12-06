from datastream import *


def start_of_packet(string):
    counter = 0
    letters_to_compare = []

    mark = False
    for character in string:
        letters_to_compare.append(character)
        counter = counter + 1
        if len(letters_to_compare) == 4:

            for letter in letters_to_compare:
                wee_chunk_1 = letters_to_compare[1:]
                wee_chunk_2 = letters_to_compare[:1]
                wee_chunk_3 = letters_to_compare[2:]
                wee_chunk_4 = letters_to_compare[:2]
                wee_chunk_5 = letters_to_compare[3:]
                wee_chunk_6 = letters_to_compare[:3]
                if letters_to_compare[0] in wee_chunk_1:
                    break
                elif (letters_to_compare[1] in wee_chunk_2
                      or letters_to_compare[1] in wee_chunk_3):
                    break
                elif (letters_to_compare[2] in wee_chunk_4
                      or letters_to_compare[2] in wee_chunk_5):
                    break
                elif letters_to_compare[3] in wee_chunk_6:
                    break
                else:
                    mark = True
            letters_to_compare.pop(0)
        if mark == True:
            break

    return counter


def start_of_packet_second_part(string):
    counter = 0
    letters_to_compare = []

    mark = False
    for character in string:
        if mark == True:
            break
        letters_to_compare.append(character)
        counter = counter + 1
        if len(letters_to_compare) == 14:
            last_item = len(letters_to_compare) - 1

            next_letter = False
            for idx, letter in enumerate(letters_to_compare):
                if next_letter == True:
                    break
                for idx_2, letter_2 in enumerate(letters_to_compare):
                    if idx_2 == idx and (idx != last_item
                                         and idx_2 != last_item):
                        continue
                    elif (letter == letter_2 and
                          ((idx != last_item and idx_2 != last_item)
                           or (idx == last_item and idx_2 != last_item)
                           or (idx != last_item and idx_2 == last_item))):
                        next_letter = True
                        break
                    elif idx == last_item and idx_2 == last_item:
                        mark = True

            letters_to_compare.pop(0)
            if mark == True:
                break

    return counter


print(start_of_packet(buffer))
print(start_of_packet_second_part(buffer))

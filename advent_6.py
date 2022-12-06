from datastream import *


def start_of_packet(string):
    counter = 0
    letters_to_compare = []

    mark = False
    for character in string:
        letters_to_compare.append(character)
        counter = counter + 1
        if len(letters_to_compare) == 4:
            print(letters_to_compare)
            for letter in letters_to_compare:
                chunk_1 = letters_to_compare[1:]
                chunk_2 = letters_to_compare[:1]
                chunk_3 = letters_to_compare[2:]
                chunk_4 = letters_to_compare[:2]
                chunk_5 = letters_to_compare[3:]
                chunk_6 = letters_to_compare[:3]
                if letters_to_compare[0] in chunk_1:
                    break
                elif letters_to_compare[1] in chunk_2 or letters_to_compare[1] in chunk_3:
                    break
                elif letters_to_compare[2] in chunk_4 or letters_to_compare[2] in chunk_5:
                    break
                elif letters_to_compare[3] in chunk_6:
                    break
                else:
                    mark = True
            letters_to_compare.pop(0)
        if mark == True:
            break

    return counter


print(start_of_packet(buffer))

'''
            if letters_to_compare[0] in letters_to_compare[1:]:
                break
            elif letters_to_compare[1] in letters_to_compare[1:]:
                break
            elif letters_to_compare[2] in letters_to_compare[1:]:
                break
            elif letters_to_compare[3] in letters_to_compare[1:]:
                break
            '''

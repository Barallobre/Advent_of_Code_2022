from rucksacks import *
import string
# Lowercase item types a through z have priorities 1 through 26.
# Uppercase item types A through Z have priorities 27 through 52.

element = ''
rucksacks = []
nums_to_sum = []

for character in items:
    if character != '\n':
        element = element + character
    if character == '\n':
        rucksacks.append(element)
        element = ''

print(rucksacks)

alphabet = list(string.ascii_letters)
print(alphabet)
print(len(alphabet))
count_odds = 0
first_half = ''
second_half = ''
half_number = 0
points = 0
for rucksack in rucksacks:
    print(rucksack + ' ' + str(len(rucksack)))
    half_number = int(len(rucksack)/2)
    first_half = rucksack[0: half_number]
    second_half = rucksack[half_number:]
    print(first_half + ' ' + str(len(first_half)))
    print(second_half + ' ' + str(len(second_half)))
    repeated_character = ''

    for character in first_half:
        if repeated_character != '':
            break
        for character2 in second_half:
            if character == character2:
                repeated_character = character
                points = points + ((alphabet.index(character))+1)
                print(character)
                print((alphabet.index(character))+1)
                break

print(points)

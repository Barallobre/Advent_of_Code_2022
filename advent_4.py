from assigments import *

element = ''
pairs_of_work = []

for character in pairs:
    if character != '\n':
        element = element + character
    if character == '\n':
        pairs_of_work.append(element)
        element = ''

print(pairs_of_work)

elf_1_numbers = ''
elf_2_numbers = ''
elf_1_individual_numbers = []
elf_2_individual_numbers = []

not_matches = 0
matches = len(pairs_of_work)
for pair in pairs_of_work:
    splited = pair.split(',')
    print(splited)
    elf_1_numbers = splited[0].split('-')
    elf_2_numbers = splited[1].split('-')
    print(elf_1_numbers)
    print(elf_2_numbers)

    for elf_1 in range(int(elf_1_numbers[0]), (int(elf_1_numbers[1]) + 1)):
        elf_1_individual_numbers.append(elf_1)
    print(elf_1_individual_numbers)

    for elf_2 in range(int(elf_2_numbers[0]), (int(elf_2_numbers[1]) + 1)):
        elf_2_individual_numbers.append(elf_2)
    print(elf_2_individual_numbers)

    if len(elf_1_individual_numbers) <= len(elf_2_individual_numbers):
        for number in elf_1_individual_numbers:
            if number not in elf_2_individual_numbers:
                not_matches = not_matches + 1
                break
    else:
        for number in elf_2_individual_numbers:
            if number not in elf_1_individual_numbers:
                not_matches = not_matches + 1
                break

    matches = matches - not_matches
    not_matches = 0
    print(matches)
    elf_1_individual_numbers = []
    elf_2_individual_numbers = []

overlaps = 0
overlaps_per_pair = 0
for pair in pairs_of_work:
    splited = pair.split(',')
    print(splited)
    elf_1_numbers = splited[0].split('-')
    elf_2_numbers = splited[1].split('-')
    print(elf_1_numbers)
    print(elf_2_numbers)

    for elf_1 in range(int(elf_1_numbers[0]), (int(elf_1_numbers[1]) + 1)):
        elf_1_individual_numbers.append(elf_1)
    print(elf_1_individual_numbers)

    for elf_2 in range(int(elf_2_numbers[0]), (int(elf_2_numbers[1]) + 1)):
        elf_2_individual_numbers.append(elf_2)
    print(elf_2_individual_numbers)

    if elf_1_individual_numbers[0] <= elf_2_individual_numbers[0]:
        for number in elf_1_individual_numbers:
            if number in elf_2_individual_numbers:
                overlaps = overlaps + 1
                break

    else:
        for number in elf_2_individual_numbers:
            if number in elf_1_individual_numbers:
                overlaps = overlaps + 1
                break

    elf_1_individual_numbers = []
    elf_2_individual_numbers = []

print(overlaps)

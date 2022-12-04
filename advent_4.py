from assigments import *

element = ''
pairs_of_work = []

for character in pairs:
    if character != '\n':
        element = element + character
    if character == '\n':
        pairs_of_work.append(element)
        element = ''

elf_1_numbers = ''
elf_2_numbers = ''
elf_1_individual_numbers = []
elf_2_individual_numbers = []


def addNumbers_to_list(numbers):
    individual_numbers = []
    for elf_1 in range(int(numbers[0]), (int(numbers[1]) + 1)):
        individual_numbers.append(elf_1)
    return individual_numbers


def overlaps_per_pair(elf_1_individual_numbers, elf_2_individual_numbers):
    overlaps = 0
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
    return overlaps


def not_matches_per_pair(elf_1_individual_numbers, elf_2_individual_numbers):
    not_matches = 0
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
    return not_matches


def split_numbers(pair):
    splited = pair.split(',')
    elf_1_numbers = splited[0].split('-')
    elf_2_numbers = splited[1].split('-')
    return elf_1_numbers, elf_2_numbers


def matches_total():
    not_matches_pair = 0

    matches = len(pairs_of_work)
    for pair in pairs_of_work:

        elf_1_numbers = split_numbers(pair)[0]
        elf_2_numbers = split_numbers(pair)[1]

        elf_1_individual_numbers = addNumbers_to_list(elf_1_numbers)
        elf_2_individual_numbers = addNumbers_to_list(elf_2_numbers)

        not_matches_pair = not_matches_per_pair(
            elf_1_individual_numbers, elf_2_individual_numbers)

        matches = matches - not_matches_pair

        elf_1_individual_numbers = []
        elf_2_individual_numbers = []
    return matches


def overlaps_total():
    overlaps_pair = 0
    overlaps = 0
    for pair in pairs_of_work:
        elf_1_numbers = split_numbers(pair)[0]
        elf_2_numbers = split_numbers(pair)[1]

        elf_1_individual_numbers = addNumbers_to_list(elf_1_numbers)
        elf_2_individual_numbers = addNumbers_to_list(elf_2_numbers)

        overlaps_pair = overlaps_per_pair(
            elf_1_individual_numbers, elf_2_individual_numbers)
        elf_1_individual_numbers = []
        elf_2_individual_numbers = []
        overlaps = overlaps + overlaps_pair
    return overlaps


matches = 0
matches = matches_total()
print(matches)
overlaps = 0
overlaps = overlaps_total()
print(overlaps)

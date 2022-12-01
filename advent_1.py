from numbers import *

element = ''
individual_numbers = []
nums_to_sum = []

for character in numbers:
    if character != '\n':
        element = element + character
    if character == '\n':
        individual_numbers.append(element)
        element = ''

totals = 0
totals_sums = []

for individual in individual_numbers:
    if individual != '':
        totals = totals + int(individual)
    if individual == '':
        totals_sums.append(totals)
        totals = 0

print(totals_sums)

totals_sums_clone = totals_sums.copy()

max_number_1 = max(totals_sums_clone)
print('The first highest number -> ' + str(max_number_1))
totals_sums_clone.remove(max_number_1)

max_number_2 = max(totals_sums_clone)
print('The seconde highest number -> ' + str(max_number_2))
totals_sums_clone.remove(max_number_2)

max_number_3 = max(totals_sums_clone)
print('The third highest number -> ' + str(max_number_3))

total_max_three = max_number_1 + max_number_2 + max_number_3
print('Sum of the three highest numbers -> ' + str(total_max_three))

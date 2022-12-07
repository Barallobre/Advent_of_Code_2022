from file_system import *
from data_arranger import *
import string
commands = data_arrange(commands)

pair_commands = []
for command in commands:
    if command[0] == '$':
        command = command.replace('$ ', '')
    pair_commands.append(command.split())
alphabet = list(string.ascii_letters)


for pair_command in pair_commands:
    if pair_command[0][0] not in alphabet:
        pair_command[0] = int(pair_command[0])
        pair_command.pop(1)

size_per_directory = []
sizes = []
sum_of_size = 0
for idx, pair_command in enumerate(pair_commands):
    if pair_command[0] == 'cd' and pair_command[1] != '..':
        size_per_directory.append(pair_command[1])
        second_loop_beginning = pair_commands[idx:]
        for idx_2, pair_command in enumerate(second_loop_beginning):
            if idx_2 == 0 and pair_command[0] == 'cd':
                continue

            if type(pair_command[0]) == int:
                sum_of_size = sum_of_size + pair_command[0]
            if pair_command[0] == 'cd' or idx_2 == len(second_loop_beginning) - 1:
                size_per_directory.append(sum_of_size)
                sizes.append(size_per_directory)
                sum_of_size = 0
                size_per_directory = []
                break

print(sizes)
directory_and_sons = {
}
sons = []
directory = ''
for idx, pair_command in enumerate(pair_commands):
    if pair_command[0] == 'cd' and pair_command[1] != '..':
        if directory != '' and sons != []:
            sons = list(set(sons))
            directory_and_sons[directory] = sons
        sons = []
        directory = ''
        directory = pair_command[1]
    if pair_command[0] == 'ls':
        for idx_2, pair_command in enumerate(pair_commands[idx:]):
            if pair_command[0] == 'dir':
                sons.append(pair_command[1])

sums = []
individual_sum = []
sum_of_dir = 0
for directory, sons in directory_and_sons.items():
    print(directory)
    print(len(sons))
    individual_sum.append(directory)
    for size in sizes:
        if size[0] == directory:
            sum_of_dir = sum_of_dir + size[1]
        elif size[0] in sons:
            sum_of_dir = sum_of_dir + size[1]
    individual_sum.append(sum_of_dir)
    sums.append(individual_sum)
    individual_sum = []
    sum_of_dir = 0

for idx, size in enumerate(sizes):
    for idx_2, sum in enumerate(sums):
        length = len(sums) - 1
        if size[0] == sums[idx_2][0]:
            break
        elif idx_2 == length:
            sums.append(size)

total_sum = 0

for sum in sums:
    if sum[1] <= 100000:
        total_sum = total_sum + sum[1]

print(sums)
print(len(sums))
print(total_sum)

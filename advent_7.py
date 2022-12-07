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
pointer = ''

for pair_command in pair_commands:
    if pair_command[0][0] not in alphabet:
        pair_command[0] = int(pair_command[0])
        pair_command.pop(1)

for pair_command in pair_commands:
    if pair_command[0] == 'cd':
        pointer = pair_command[1]
    print(pair_command)

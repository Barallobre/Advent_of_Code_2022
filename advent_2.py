from strategy_plan import *

# 1 for Rock, 2 for Paper, and 3 for Scissors
# 0 if you lost, 3 if the round was a draw, and 6 if you won
# A for Rock, B for Paper, and C for Scissors
# X for Rock, Y for Paper, and Z for Scissors

element = ''
plays = []
nums_to_sum = []

for character in games:
    if character != '\n':
        element = element + character
    if character == '\n':
        plays.append(element)
        element = ''

print(plays)
points = 0
total_points = 0
for play in plays:
    print(play)
    him = play[0]
    me = play[-1]

    if me == 'X':
        points = points + 1
        if him == 'A':
            points = points + 3
        elif him == 'C':
            points = points + 6
    elif me == 'Y':
        points = points + 2
        if him == 'A':
            points = points + 6
        elif him == 'B':
            points = points + 3
    elif me == 'Z':
        points = points + 3
        if him == 'B':
            points = points + 6
        elif him == 'C':
            points = points + 3

    total_points = total_points + points
    print(points)
    points = 0

print(total_points)

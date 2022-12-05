
def data_arrange(data):
    element = ''
    plays = []

    for single_data in data:
        if single_data != '\n':
            element = element + single_data
        if single_data == '\n':
            plays.append(element)
            element = ''
    return plays

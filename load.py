def load_numbers(file_name):
    numbers = []

    with open (file_name) as f:
        for line in f:
            numbers.append(int(line))
    
    return numbers

def load_strings(filename):
    strings = []

    with open(filename) as f:
        for line in f:
            strings.append(line.rstrip())
    return strings
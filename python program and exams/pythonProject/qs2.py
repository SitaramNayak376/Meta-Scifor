import re

def check_numerical_values():
    with open("D:\\bbb.txt", 'r') as file:
        lines = file.readlines()

    pattern = re.compile(r'\d+')

    for line_number, line in enumerate(lines, start=1):
        if pattern.search(line):
            print("Line ", line_number, line.strip())



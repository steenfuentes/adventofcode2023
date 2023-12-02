cal_values: list = []

with open('input.txt') as f:
    for line in f:
        digits = [int(d) for d in line.strip() if d.isdigit()]

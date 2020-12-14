expenses = {}

with open('01.txt')as input_file:
    for line in input_file:
        num = int(line)
        if num in expenses:  # matching number already seen - do calc
            print(f"Part 1: {num * expenses[num]}")
        else:
            expenses[2020 - num] = num

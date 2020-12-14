expenses = {}

with open('01.txt') as input_file:
    # Part 1
    for line in input_file:
        num = int(line)
        if num in expenses:  # matching number already seen - do calc
            print(f"Part 1: {num * expenses[num]}")

        expenses[2020 - num] = num

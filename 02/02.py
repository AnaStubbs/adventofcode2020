num_passwords_valid_p1 = 0
num_passwords_valid_p2 = 0

with open('02.txt') as input_file:
    # Part 1
    for line in input_file:
        line_segments = line.split()

        char_range = [int(num) for num in line_segments[0].split("-")]
        char_to_match = line_segments[1][0]
        password = line_segments[2]

        number_of_matches = sum(1 for char in filter(lambda x: x is char_to_match, password))

        if char_range[0] <= number_of_matches <= char_range[1]:
            num_passwords_valid_p1 += 1

print(f"Part 1: {num_passwords_valid_p1}, Part 2: {num_passwords_valid_p2}")

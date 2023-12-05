def is_numeric(x):
    try:
        int(x)
        return True
    except ValueError:
        return False


def is_symbol(x):
    return x != '.' and not is_numeric(x)


def get_spaces_around_one_character(line_number, i):
    return [
        (line_number - 1, i - 1), (line_number - 1, i), (line_number - 1, i + 1),
        (line_number, i - 1),                           (line_number, i + 1),
        (line_number + 1, i - 1), (line_number + 1, i), (line_number + 1, i + 1),
    ]


class SchematicNumber:
    def __init__(self, line_number, start_position, end_position, value, lines_end, line_end):
        self.line_number = line_number
        self.start_position = start_position
        self.end_position = end_position
        self.number_positions = [(line_number, line_position) for line_position in range(self.start_position, self.end_position)]
        self.value = value
        self.has_near_symbol = False
        self.surrounding_spaces = []
        self.limit_line_start = 0
        self.limit_line_end = line_end
        self.limit_lines_start = 0
        self.limit_lines_end = lines_end
        self.gear_positions = []

        self.get_valid_surrounding_spaces()

    def clean_surrounding_spaces(self):

        self.surrounding_spaces = list(set(self.surrounding_spaces))

        for space in list(self.surrounding_spaces):
            if (
                    (space[0] < self.limit_lines_start) or
                    (space[0] > self.limit_lines_end) or
                    (space[1] < self.limit_line_start) or
                    (space[1] > self.limit_line_end)
            ):
                self.surrounding_spaces.remove(space)

            elif space in self.number_positions:
                self.surrounding_spaces.remove(space)

    def get_valid_surrounding_spaces(self):
        for i in range(self.start_position, self.end_position):
            self.surrounding_spaces.extend(get_spaces_around_one_character(self.line_number, i))

        self.clean_surrounding_spaces()

    def check_surrounding_spaces(self, lines):
        ...


with open('./schematic', 'r') as f:
    lines = [line.strip() for line in f.readlines()]

number_positions = []
symbol_positions = []
numbers = []

for i, line in enumerate(lines):
    j = 0
    line_limit = len(line) - 1
    while j <= line_limit:
        k = j
        c = line[j]
        still_numeric = True

        if is_symbol(c):
            symbol_positions.append((i, j))
            j += 1

        elif is_numeric(c):
            while still_numeric:
                j += 1
                if j > line_limit:
                    break
                still_numeric = is_numeric(line[j])

            lines_end, line_end = len(lines), line_limit

            numbers.append(SchematicNumber(i, k, j, line[k:j], lines_end, line_end))

        else:
            j += 1


potential_gear_positions = []
for position in symbol_positions:
    if lines[position[0]][position[1]] == '*':
        potential_gear_positions.append(position)

potential_numbers_near_gears = []
for number in numbers:
    for space in number.surrounding_spaces:
        if space in potential_gear_positions:
            number.gear_positions.append(space)
            potential_numbers_near_gears.append(number)
            break

gear_dict = {}
for number in potential_numbers_near_gears:
    gear_position = number.gear_positions[0]

    if gear_position not in gear_dict.keys():
        gear_dict[gear_position] = [number]
    else:
        gear_dict[gear_position].append(number)


valid_gears = {}
for gear in gear_dict.keys():
    if len(gear_dict[gear]) == 2:
        valid_gears[gear] = gear_dict[gear]

ratios = []
for gear in valid_gears:
    ratios.append(int(valid_gears[gear][0].value) * int(valid_gears[gear][1].value))

print(sum(ratios))




























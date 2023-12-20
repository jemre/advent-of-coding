def is_numeric(x):
    try:
        int(x)
        return True
    except ValueError:
        return False


def parse_map_values(line):
    destination_start, source_start, num_steps = [int(i) for i in line.split()]
    source_range = (range(source_start, source_start + num_steps))
    destination_range = range(destination_start, destination_start + num_steps)

    return [source_range, destination_range]


def parse_key(line):
    split = line.split('-')
    return split[0], split[-1].split()[0]


def get_seeds(line):
    return line.split()[1:]


with open('./almanac', 'r') as f:
    lines = [line.strip() for line in f.readlines()]

key_mapping = {}
full_mapping = {}
seeds = []

current_key = 'there_was_a_problem'
for line in lines:
    if line == '':
        continue

    if line[:5] == 'seeds':
        seeds = get_seeds(line)

    elif not is_numeric(line[0]):
        keys = parse_key(line)
        current_key = keys[1]
        key_mapping[keys[0]] = keys[1]
        full_mapping[current_key] = [[], []]

    elif is_numeric(line[0]):
        map_values = parse_map_values(line)
        full_mapping[current_key][0].append(map_values[0])
        full_mapping[current_key][1].append(map_values[1])

    else:
        raise Exception('Unexpected line!')


def traverse_map(start_value, start, end, key_mapping, full_mapping):
    at_end = False
    value = start_value
    key = start
    while not at_end:
        map = full_mapping[key_mapping[key]]
        found = False
        for i, source in enumerate(map[0]):
            if value in source:
                j = source.index(value)
                found = True
                break
        if found:
            value = map[1][i][j]
            # print('found', 'key', key, 'value', value)
        else:
            value = value

        key = key_mapping[key]
        if key == end:
            at_end = True

    return value

seeds_map = {}
actual_seed_ids = [int(seed) for seed in seeds[::2]]
actual_seed_ranges = [int(seed) for seed in seeds[1::2]]

for i, seed in enumerate(actual_seed_ids):
    seeds_map[seed] = range(seed, seed + actual_seed_ranges[i], 1)

locations = []
for seed_key in seeds_map.keys():
    seed_range = seeds_map[seed_key]
    for seed in seed_range:
        location = traverse_map(int(seed), 'seed', 'location', key_mapping, full_mapping)
        locations.append(location)

print(min(locations))


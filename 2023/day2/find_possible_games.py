def multiply_list(l):
    result = l[0]
    for i in l[1:]:
        result *= i
    return result


with open('./game_input', 'r') as f:
    game_data = {}

    games_out_of_limit = []

    for line in f.readlines():
        line = line.strip()

        game_num = int(line.split(':')[0].split(' ')[1])

        game_values = [j.split(', ') for j in [i.strip() for i in line.split(':')[1].split(';')]]

        game_data[game_num] = {}

        for vals in game_values:
            for pair in vals:
                num, color = pair.strip().split(' ')
                if color in game_data[game_num].keys():
                    if int(num) > int(game_data[game_num][color]):
                        game_data[game_num][color] = int(num)
                else:
                    game_data[game_num][color] = int(num)

    print(sum([multiply_list(list(game_data[game_num].values())) for game_num in [game_num for game_num in game_data.keys()]]))




with open('./game_input', 'r') as f:

    limits = {'red': 12, 'green': 13, 'blue': 14}

    game_data = {}

    games_out_of_limit = []

    for line in f.readlines():
        line = line.strip()

        game_num = int(line.split(':')[0].split(' ')[1])

        game_values = [j.split(', ') for j in [i.strip() for i in line.split(':')[1].split(';')]]

        game_data[game_num] = {}

        for vals in game_values:
            # print('vals', vals)
            for pair in vals:
                # print('pair', pair)
                num, color = pair.strip().split(' ')
                if color in game_data[game_num].keys():
                    if int(num) > int(game_data[game_num][color]):
                        game_data[game_num][color] = int(num)
                else:
                    game_data[game_num][color] = int(num)

        # print(line)
        # print(game_data[game_num])
        # break

    for game_num in game_data.keys():
        for color in game_data[game_num].keys():
            if int(game_data[game_num][color]) > limits[color]:
                games_out_of_limit.append(int(game_num))


    games_out_of_limit = set(games_out_of_limit)

    in_limits = [i for i in game_data.keys() if i not in games_out_of_limit]

    print(in_limits)

    print(sum(in_limits))
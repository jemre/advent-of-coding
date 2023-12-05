word_num_map = {
    'zero': '0',
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}

with open('./encoded_calibrations', 'r') as f:
    calibration_list = []
    for line in f.readlines():
        line = line.strip()

        nums = []

        for i, c in enumerate(line):

            for word in word_num_map.keys():
                if word == line[i: i+len(word)]:
                    nums.append(word_num_map[word])
                    break

            try:
                num = str(int(c))
                nums.append(num)
            except ValueError:
                continue

        calibration_list.append(nums)

print(calibration_list)

cal_sum = 0

for cal in calibration_list:
    cal_sum += int(cal[0]+cal[-1])

print(cal_sum)

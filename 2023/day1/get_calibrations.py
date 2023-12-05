with open('./encoded_calibrations', 'r') as f:
    calibration_list = []
    for line in f.readlines():
        line = line.strip()

        nums = []

        for c in line:
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

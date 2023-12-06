with open('./scratch_cards', 'r') as f:
    lines = [line.strip() for line in f.readlines()]


cards = {}

for line in lines:
    card_num = line.split(':')[0].split()[1]
    winning_nums = line.split(':')[1].strip().split('|')[0].strip().split()
    have_nums = line.split(':')[1].strip().split('|')[1].strip().split()

    matched_nums = [have_num for have_num in have_nums if have_num in winning_nums]

    if len(matched_nums) == 0:
        worth = 0
    else:
        worth = 2**(len(matched_nums)-1)

    cards[card_num] = {'winning_nums': winning_nums, 'have_nums': have_nums, 'matched_nums': matched_nums, 'worth': worth}

for card in cards.keys():
    print(cards[card])

print(sum([cards[card]['worth'] for card in cards.keys()]))


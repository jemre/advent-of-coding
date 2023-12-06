with open('./scratch_cards', 'r') as f:
    lines = [line.strip() for line in f.readlines()]


cards = {}

for line in lines:
    card_num = int(line.split(':')[0].split()[1])
    winning_nums = line.split(':')[1].strip().split('|')[0].strip().split()
    have_nums = line.split(':')[1].strip().split('|')[1].strip().split()

    matched_nums = [have_num for have_num in have_nums if have_num in winning_nums]

    if len(matched_nums) == 0:
        worth = 0
    else:
        worth = 2**(len(matched_nums)-1)

    cards[card_num] = {
        'winning_nums': winning_nums,
        'have_nums': have_nums,
        'matched_nums': matched_nums,
        'worth': worth,
        'num_copies': 0
    }

max_card_num = 220
for card in cards.keys():
    num_matched = len(cards[card]['matched_nums'])
    for j in range(cards[card]['num_copies'] + 1):
        for i in range(card + 1, card + num_matched + 1):
            if i > max_card_num:
                break
            else:
                cards[i]['num_copies'] += 1

print(sum([cards[card]['num_copies'] for card in cards.keys()]) + max_card_num)



import re

lines = open("data.txt", "r").read().splitlines()

value = 0
cards = [1 for _ in lines]

for line in lines:
    numbers_dict = {}
    card_id = int(re.findall(r'Card\s+(\d+):', line)[0])
    sides = line.split("|")
    left_side_winning = sides[0].split()
    right_side_number_you_have = sides[1].split()
    card_matches = 0

    for number in right_side_number_you_have:
        if number in left_side_winning:
            card_matches = card_matches + 1

    if card_matches > 0:
        value += 2 ** (card_matches - 1)

    for i in range(card_matches):
        cards[card_id + i] += cards[card_id - 1]

print(value)
print(sum(cards))

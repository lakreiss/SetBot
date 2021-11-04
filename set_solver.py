from set_card import SetCard

# NUMBER:SHAPE:SHADE:COLOR
# [123][osd][sef][prg]

board = ['2ssg', '1deg', '1oeg',
         '2sep', '2dfg', '1osr',
         '3deg', '1ofr', '2dsr',
         '1ssg', '2dsp', '3ssp',
         '1dfp', '1sfr', '2sfg',
        ]
cards = [SetCard(card) for card in board]

def find_match(all_cards):
    for i in range(len(all_cards)):
        for j in range(i + 1, len(all_cards)):
            for k in range(j + 1, len(all_cards)):
                cards = [all_cards[i], all_cards[j], all_cards[k]]
                numbers = set([card.number for card in cards])
                colors = set([card.color for card in cards])
                shapes = set([card.shape for card in cards])
                shades = set([card.shade for card in cards])
                if (len(numbers) == 1 or len(numbers) == 3) and (len(colors) == 1 or len(colors) == 3) and (len(shapes) == 1 or len(shapes) == 3) and (len(shades) == 1 or len(shades) == 3):
                    return cards
    return None

for card in find_match(cards):
    print(str(card))
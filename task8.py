cards = {2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 0, 8: 0, 9: 0, 10: -1, 'J': -1, 'Q': -1, 'K': -1, 'A': -1}
summ_cards = 0
for key in cards:
    summ_cards += cards[key]
    print(f'Changed: {summ_cards}')
print(summ_cards)
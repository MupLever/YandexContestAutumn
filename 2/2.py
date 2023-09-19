def push(deck, number, card) -> int:
    if card not in deck:
        deck[card] = [0, 0]
    diff = abs(deck[card][0] - deck[card][1])
    deck[card][number] += 1
    if abs(deck[card][0] - deck[card][1]) > diff:
        return 1
    return -1

def pop(deck, number, card):
    diff = abs(deck[card][0] - deck[card][1])
    deck[card][number] -= 1
    if abs(deck[card][0] - deck[card][1]) > diff:
        return 1
    return -1

_, _, action_count = map(int, input().split(' '))

both_decks = dict()
for card in input().split(' '):
    push(both_decks, 0, card)

for card in input().split(' '):
    push(both_decks, 1, card)

count = 0
for value in both_decks.values():
    count += abs(value[0] - value[1])

for _ in range(action_count):
    action, player, card = input().split(' ')
    if player == 'A':
        number = 0
    else:
        number = 1

    if int(action) == 1:
        count += push(both_decks, number, card)
    else:
        count += pop(both_decks, number, card)

    print(count, end=' ')

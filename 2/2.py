def push(deck, number, card):
    if card not in deck:
        deck[card] = [0, 0]
    deck[card][number] += 1

def pop(deck, number, card):
    deck[card][number] -= 1

_, _, action_count = map(int, input().split(' '))

both_decks = dict()
for card in input().split(' '):
    push(both_decks, 0, card)
for card in input().split(' '):
    push(both_decks, 1, card)

for _ in range(action_count):
    action, player, card = input().split(' ')
    if player == 'A':
        number = 0
    else:
        number = 1

    if int(action) == 1:
        push(both_decks, number, card)
    else:
        pop(both_decks, number, card)
        
    count = 0
    
    for value in both_decks.values():
        first = value[0]
        second = value[1]
        m = max(first, second)
        count += max(m - first, m - second)

    print(count, end=' ')
    
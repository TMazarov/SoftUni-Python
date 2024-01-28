def faro_shuffle(cards, shuffles):
    deck = cards.split()

    for _ in range(shuffles):
        split_index = len(deck) // 2
        first_half = deck[:split_index]
        second_half = deck[split_index:]

        shuffled_deck = [card for pair in zip(first_half, second_half) for card in pair]
        deck = shuffled_deck

    return deck


cards_input = input()
shuffles = int(input())

result = faro_shuffle(cards_input, shuffles)
print(result)

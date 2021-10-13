import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                                        for rank in self.ranks]
    
    def __len__(self):
        return len(self._cards)
    
    def __getitem__(self, position):
        return self._cards[position]

print('\nNew card:')
beer_card = Card('7', 'diamonds')
print(beer_card)

print('\nAll cards count:')
deck = FrenchDeck()
print(len(deck))

print('\nFirst & Last cards:')
print(deck[0])
print(deck[-1])

print('\nPick up three cards:')
from random import choice
print(choice(deck))
print(choice(deck))
print(choice(deck))

print('\nTop 3 cards:')
print(deck[:3])

print('\nAll ace cards:')
print(deck[12::13])

print('\nAll card:')
for card in deck:
    print(card)
    print(FrenchDeck.ranks.index(card.rank))

print('\nAll card reversed:')
for card in reversed(deck):
    print(card)

print('\nIf Q hearts in deck:')
print(Card('Q', 'hearts') in deck)

print('\nIf 7 beasts in deck:')
print(Card('7', 'beasts') in deck)

print('\nSort:')
suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)
print(len(suit_values))
def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    print(card)
    print(str(rank_value) + '*' + str(len(suit_values)) + '+' + str(suit_values[card.suit]))
    print(rank_value * len(suit_values) + suit_values[card.suit])
    return rank_value * len(suit_values) + suit_values[card.suit]

for card in sorted(deck, key=spades_high):
    print(card)
"""
知识点：namedtuple __len__, __getitem__

"""
import collections
from random import choice

Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        """
        实现该方法后，则变成可迭代了
        :param position:
        :return:
        """
        # print("return item")
        return self._cards[position]



def sample_01():
    beer_card = Card('7', 'diamonds')
    print(beer_card)
    deck = FrenchDeck()
    print(len(deck))
    print(deck[0])
    print(deck[-1])
    print("=========================")
    card = choice(deck)
    print(card)
    #  查看最上面3张牌
    list01 = deck[:3]
    print(list01)
    #  抽取第12张牌，然后每隔13张抽取一张
    print("=========2================")
    list02 = deck[12::13]
    print(list02)
    print("=========3================")
    for card in deck:
        print(card)
    for card in reversed(deck): #doctest: +ELLIPSIS
        print(card)
    result = Card('Q', 'hearts') in deck
    print(result)
    result2 = Card('7', 'beats') in deck
    print(result2)


def spades_high(card):
    suit_values = dict(spade=3, hearts=2, diamonds=1, club=0)
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values)



if __name__ == '__main__':
    sample_01()


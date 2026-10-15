from cmput274 import *

'''
A Rank is
 - a str in ("2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace")
'''

'''
A Suit is
 - a str in ("Diamonds", "Clubs", "Hearts", "Spades")
'''

'''
A Card is a
 - LL(Suit, Rank)
'''

def compareSuit(c1, c2)
  sc1 = first(c1)
  sc2 = first(c2)
  if sc1 == "Diamonds":
    return sc2 != "Diamonds"
  if sc1 == "Clubs":
    return sc2 == "Hearts" or sc2 == "Spades"
  if sc1 == "Hearts":
    return sc2 == "Spades"
  return False


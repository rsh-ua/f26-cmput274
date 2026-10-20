from cmput274 import *

'''
A Rank is
 - a Nat in [2,14]
'''

'''
A Suit is
 - a Nat in [0,3]
'''

'''
A Card is a
 - LL(Suit, Rank)
'''

def compareSuit(c1, c2):
  sc1 = first(c1)
  sc2 = first(c2)
  return sc1 < sc2

def compareRank(c1, c2):
  second = lambda l: first(rest(l))
  rc1 = second(c1)
  rc2 = second(c2)
  return rc1 < rc2

def compareCard(c1, c2):
  return compareSuit(c1,c2) or (not compareSuit(c2,c1) and compareRank(c1,c2))

from cmput274 import *

def selectExtreme(elem, pair):
  if elem < first(pair):
    # if elem is less than the smallest seen so far... it is now the smallest seen
    # so far
    return cons(elem, rest(pair)) # (elem, p1)
  if elem > first(rest(pair)):
    # elem is larger than the largest seen so far it is now our largest seen so far
    return LL(first(pair), elem) # (p0, elem)
  return pair

def findExtremes(l):
  '''
  findExtremes produces a pair of the form (vi, vj) where vi
    is the minimal element in l and vj is the maximal element in l
  '''
  return foldl(l, selectExtreme, LL(first(l), first(l))) # -> (minElem, maxElem)

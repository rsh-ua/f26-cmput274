from cmput274 import *

def filter(pred, l):
  '''
  filter produces the LList that is the result of filtering l with the given predicate

  pred    - (X -> bool)
  l       - LList of X
  returns - LList of X

  Examples:
    def isNeg(x):
      return x < 0

    filter(isNeg, LL(-10, 5, 0, -2)) -> LL(-10, -2)
  '''
  if isEmpty(l):
    return empty()
  v0 = first(l)
  ror = filter(pred, rest(l)) # -> the filtered rest of the list
  if pred(v0):
    return cons(v0, ror)
  return ror

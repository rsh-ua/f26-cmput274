from cmput274 import *

def getIth(l, i):
  '''
  getIth returns the ith element of the LList l

  l       - a LList of Any of at least length i+1
  i       - a Nat
  returns - an Any

  Examples:
    getIth(cons(5, cons(3, cons(2, empty()))), 0) -> 5
    getIth(cons(5, cons(3, cons(2, empty()))), 1) -> 3
    getIth(cons(5, cons(3, cons(2, empty()))), 2) -> 2
  '''
  if i == 0:
    return first(l)
  # I need get closer to my base case of i == 0
  # BUT I must also ensure that when I reach that case
  # that first(l) is the item I want!
  # We observer that the ith item of a LList L
  # is the same thing as the i-1th item of rest(L) (for i>0)
  return getIth(rest(l), i-1)

from cmput274 import *


def isSorted(t):
  # returns true if L is either non-increasing OR non-decreasing
  def isNonIncreasing(i):
    if i >= len(t)-1: # Then the tuple remaining to consider is <= length 1
      return True
    return t[i] >= t[i+1] and isNonIncreasing(i+1)

  def isNonDecreasing(i):
    if i >= len(t)-1:
      return True
    return t[i] <= t[i+1] and isNonDecreasing(i+1)

  return isNonIncreasing(0) or isNonDecreasing(0)

def isOrdered(t, cmp):
  '''
  isOrdered returns true if the tuple t is ordered with respect to the
            cmp fn. That is, every pair of values in t t[i] and t[i+1]
            then cmp(t[i], t[i+1]) -> True

  t       - a Tuple of X
  cmp     - (X X -> bool)
  returns - bool

  Examples:
    isOrdered((1, 5, 10, 12), lambda x, y: x <= y) -> True
    isOrdered((10, 8, 4, 2), lambda x, y: x >= y) -> True
    isOrdered((1, 5, 10, 12), lambda x, y: x >= y) -> False
  '''
  def tupleHelper(i):
    if i >= len(t)-1:
      return True
    return cmp(t[i], t[i+1]) and tupleHelper(i+1)
  return tupleHelper(0)


def isSorted2(t):
  return isOrdered(t, lambda x, y: x <= y) or isOrdered(t, lambda x, y: x >= y)

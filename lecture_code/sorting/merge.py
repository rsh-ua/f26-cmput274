from cmput274 import *


def merge(sl1, sl2):
  '''
  merge takes two LLists sorted in non-decreasing order and
        produces the sorted result of combining both LLists

  sl1     - Sorted LList of X
  sl2     - Sorted LList of X
  returns - Sorted LList of X

  Examples:
    merge(LL(1, 6, 9), LL(7, 10, 12)) -> LL(1, 6, 7, 9, 10, 12)
    merge(LL(5, 10, 12, 15), empty()) -> LL(5, 10, 12, 15)
  '''
  # Our base case is when either LList is empty then
  # the result of merging empty() with some sorted list SL
  # is just that sorted list SL
  if isEmpty(sl1):
    return sl2
  if isEmpty(sl2):
    return sl1
  if first(sl1) < first(sl2):
    # Add the first(sl1) to the front of our new hand (ror)
    return cons(first(sl1), merge(rest(sl1), sl2))
  return cons(first(sl2), merge(sl1, rest(sl2))

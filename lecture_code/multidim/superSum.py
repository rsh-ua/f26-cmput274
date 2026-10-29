from cmput274 import *
def sumSuperList(sl):
  '''
  sumSuperList return the sum of all integers in the
    SuperLList
  sl - SuperLList of ints
  returns - int
  Example:
    sumSuperList(LL(5, 3, LL(2, LL(1, 4), LL(6)), LL(LL(LL(LL(1)))))) -> 22
  '''
  if isEmpty(sl):
    return 0
  if type(first(sl)) == int:
    # If the first of sl is an int... then processing it just means
    # adding it to the recursive result.
    return first(sl) + sumSuperList(rest(sl))
  if type(first(sl)) == LList:
    # If the first of sl is a SuperLList of Nat then processing it means
    # adding /every/ number within it, no matter how nested, to the sum of
    # recursive result. But adding every number within it is a non-trivial task!
    # If only we had a function which took a SuperLList of Int and returned the
    # sum of all numbers in it...
    # but we do! The one we're writing!
    return  sumSuperList(first(sl)) + sumSuperList(rest(sl))

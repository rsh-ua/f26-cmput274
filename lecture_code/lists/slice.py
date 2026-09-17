from cmput274 import *

def slice(l, start, end):
  '''
  slice returns the subllist of a llist of the range [start,end)

  l       - a LList of Any
  start   - an integer < length of l
  end     - an integer <= length of l
  returns - a LList of Any

  Examples:
    slice(cons(5,cons(4,cons(3,cons(2,cons(1,cons(0,cons(-1,empty()))))))), 1, 3)
      -> cons(4,cons(3,empty())

  '''
  if start != 0:
    # Observation... we can only grab the first element of a LList
    # so if start is > 0 we can't even begin to grab the value we want!
    # however... index i of the LList (v0,v1,...,vn)
    #            is equivalently index i-1 of the LList (v1,v2,...,vn)
    return slice(rest(l), start-1, end-1)
  if end <= start:
    # If our range is [s,e) where e is <= start then we have an empty range!
    return empty()
  return cons(first(l), slice(rest(l), start, end-1))

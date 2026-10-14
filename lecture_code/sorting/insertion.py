from cmput274 import *

def insert(elem, sl):
  '''
  insert produces a new list sorted in non-decreasing
         order, the result of inserting elem into sl

  elem - X
  sl - LList of X, sorted in non-decreasing order
  returns - LList of X

  Example:
    insert(5, LL(-1, 4, 10, 20)) -> LL(-1, 4, 5, 10, 20)
  '''
  if isEmpty(sl):
    return cons(elem, empty())
  v0 = first(sl)
  if elem <= v0:
    # if elem <= v0 then it is smaller (or equal to) the smallest
    # value in my sorted LList, so it must come before all other values!
    return cons(elem, sl)
  # If the above is condition is not true then the first element of our list
  # must come /before/ the element to insert. So, we must insert the new element
  # somewhere in the rest of the LList
  ror = insert(elem, rest(sl)) # sorted LList of the rest of sl with
  # elem inserted in sorted order (v1,...,elem,vi,...,vn)
  return cons(v0, ror)

from cmput274 import *
def listCount(sl):
  '''
  listCount return the count of all LLists of sl no matter how nested
            that includes sl itself
  sl - SuperLList of X
  returns - Nat
  Example:
    listCount(LL(5, 3, LL(2, LL(1, 4), LL(6)), LL(LL(LL(LL(1)))))) ->  8
  '''
  if isEmpty(sl):
    return 1
  if type(first(sl)) == LList:
    return  listCount(first(sl)) + listCount(rest(sl))
  return listCount(rest(sl))

def flatten(sl):
  # superLList of X -> LList of X
  if isEmpty(sl):
    return empty()
  if type(first(sl)) != LList:
    return cons(first(sl), flatten(rest(sl)))
  return foldr(flatten(first(sl)), cons, flatten(rest(sl)))

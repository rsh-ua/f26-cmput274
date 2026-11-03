from cmput274 import *

def concat(l1, l2):
  if isEmpty(l1):
    return l2
  return cons(first(l1), concat(rest(l1), l2))

def findLeaves(t):
  def walkChildren(ctuple, i):
    if i >= len(ctuple):
      return empty()
    lvs = findLeaves(ctuple[i])
    ror = walkChildren(ctuple, i+1)
    return concat(lvs, ror)
  if t[1] == ():
    return LL(t[0])
  # Now need to apply findLeaves to each child in our tuple of children...
  # and we need to concatenate all those resultant lists
  return walkChildren(t[1], 0)

# An IntTree is one of
# - (Int, ())
# - (Int, non-empty tupleof(IntTree))

def findLeaves2(t):
  '''
  findLeaves returns a LList of all the ints stored in the leaf nodes of t

  t        - an IntTree
  returns  - a LList of Int

  Examples:
    ...
  '''
  if t[1] == (): # if this is a leaf node
    return LL(t[0])
  concat = lambda l1, l2: foldr(l1, cons, l2)
  answer = foldr(t[1], lambda c, ror: concat(findLeaves2(c), ror), empty())
  return answer

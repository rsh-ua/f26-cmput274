from cmput274 import *


def findPairs(t, tar):
  '''
  Construct a LList of pairs of the values in t that
  sum to tar
  '''
  def searchRest(cur, val):
    if cur >= len(t):
      return False
    if t[cur] == val:
      return True
    return searchRest(cur+1, val)
  def searchCurrent(i):
    '''
    Finds all pairs of t that sum to tar in t[i+1:]
    '''
    if i >= len(t):
      return empty()
    toFind = tar-t[i]
    if searchRest(i+1, toFind):
      # toFind exists in our tuple, and t[i] + toFind is a pair that sums to tar!
      return cons(LL(t[i], toFind), searchCurrent(i+1))
    return searchCurrent(i+1)
  return searchCurrent(0)

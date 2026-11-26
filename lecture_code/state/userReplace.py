from cmput274 import *
def replace(l, i, v):
  '''
  replace replaces the ith value of l with v

  l       - a LList of X
  i       - a Nat
  v       - an int
  returns - a LList of anyof(X, int)

  Examples:
    replace(LL(5, 4, 2, 10), 1, 3) -> LL(5, 3, 2, 10)
  '''
  def helper(numSkip, lstRemaining):
    if numSkip == 0:
      return cons(v, rest(lstRemaining))
    return cons(first(lstRemaining), helper(numSkip-1, rest(lstRemaining)))
  return helper(i, l)

def userReplace(l):
  index = int(input())
  value = int(input())
  return replace(l, index, value)

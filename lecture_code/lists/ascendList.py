from cmput274 import *

def ascendList(n):
  '''
  ascendList produces the LList from 0...n in ascending order

  n       - a Nat
  returns - a LList of Nat

  Examples:
    ascendList(3) -> (0, 1, 2, 3)
    ascendList(0) -> (0)
  '''
  if n == 0:
    return cons(0,empty())
  # n is my current element... need to do something with it
  # I want the LList (0,1,...,n)
  ror = ascendList(n-1)
  # assume our function works then ror is (0,...,n-1)
  # cons(n, ror) would then be cons(n, (0,...,n-1))
  #   which is -> (n,0,1,2,...,(n-1))
  return cons(ror, cons(n, empty()))

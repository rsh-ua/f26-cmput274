from cmput274 import *


def map(f, l):
  '''
  map maps the function f onto the LList s

  f       - (X -> Y)
  l       - LList of X
  returns - LList of Y

  Examples:
    def add3(n):
      return 3+n
    map(add3, LL(1,2,3)) -> LL(4,5,6)
  '''
  if isEmpty(l):
    return empty()
  v0 = first(l)
  ror = map(f, rest(l)) # -> (f(v1), f(v2), ..., f(vn))
  return cons(f(v0), ror)

from cmput274 import *

def skipGen(n):
  def skipN(l, step):
    if isEmpty(l):
      return empty()
    if step == n:
      return skipN(rest(l), 1)
    return cons(first(l), skipN(rest(l), step+1))
  return lambda l: skipN(l, 1)


def skipGen2(n):
  def skipN(l, i):
    if isEmpty(l):
      return empty()
    ror = skipN(rest(l), i+1)
    if i%n == n-1:
      return ror
    return cons(first(l), ror)
  return lambda l: skipN(l, 0)

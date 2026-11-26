from cmput274 import *


def strToTuple(s):
  ans = ()
  for c in s:
    ans = ans + (c,)
  return ans

def strToTuple2(s):
  ans = ()
  for c in s:
    ans = ans + (c,)
    s = s + "aaaa"
  return ans

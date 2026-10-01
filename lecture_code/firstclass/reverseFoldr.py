from cmput274 import *

def append(elem, alreadyReversed):
  return foldr(alreadyReversed, cons, cons(elem, empty()))



def reverse(l):
  return foldr(l, append, empty())

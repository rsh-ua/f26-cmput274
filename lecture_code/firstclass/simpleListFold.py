from cmput274 import *


def fold(l, combine, base):
  if isEmpty(l):
    return base
  return combine(first(l), fold(rest(l), combine, base))


def doubleAndCons(elem, lon):
  return cons(2*elem, lon)

def sumUp(elem, sor):
  return elem+sor

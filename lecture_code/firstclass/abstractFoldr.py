from cmput274 import *


def fold(s, combine, base, getRest, getFirst, checkBase):
  if checkBase(s):
    return base
  return combine(getFirst(s), fold(getRest(s), combine, base, getRest, getFirst, checkBase))


def doubleAndCons(elem, lon):
  return cons(2*elem, lon)

def sumUp(elem, sor):
  return elem+sor

def restOfString(s):
  return s[1:]

def firstOfString(s):
  return s[0]

def emptyString(s):
  return s == ""

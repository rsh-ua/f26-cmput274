from cmput274 import *

def doubleList(l):
  '''
  doubleList returns a new LList that is the result of multiplying every number in
             l by 2

  l       - a LList of Num
  returns - a LList of Num

  Examples:
    doubleList(<1,2,3>) -> <2,4,6>
  '''
  if isEmpty(l):
    return empty()
  ror = doubleList(rest(l))
  return cons(2*first(l), ror)

def combine(elem, ror):
  return cons(2*elem, ror)

def doubleList2(l):
  if isEmpty(l):
    return empty()
  return combine(first(l), doubleList2(rest(l)))

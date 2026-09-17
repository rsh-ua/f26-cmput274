from cmput274 import *

def sumOfList(lon):
  '''
  sumOfList returns the sum of a list of numbers

  lon     - a LList of Num
  returns - a Num

  Examples:
    sumOfList(cons(1, cons(2, cons(3,empty())))) -> 6
  '''
  if isEmpty(lon):
    return 0
  curVal = first(lon)
  return curVal + sumOfList(rest(lon))

def countOfList(l):
  '''
  countOfList returns the number of elements in l

  l       - a LList of Any
  returns - a Nat

  Examples:
    countOfList(cons(1,cons(2,empty()))) -> 2
    countOfList(empty()) -> 0
  '''
  if isEmpty(l):
    return 0
  return 1 + countOfList(rest(l))

def mean(lon):
  '''
  mean is meant to return the mean of a list of numbers

  lon     - a non-empty LList of Num
  returns - a Float

  Examples:
    mean(cons(3.0, cons( 4.0, cons(5.0, empty())))) -> 4.0
  '''
  return sumOfList(lon)/countOfList(lon)

from cmput274 import *

second = lambda l : first(rest(l))
def bubble(l):
  if len(l) <= 1:
    return l
  if first(l) > second(l):
    newFirst = second(l)
    newRest = cons(first(l), rest(rest(l)))
    return cons(newFirst, bubble(newRest))
  return cons(first(l), bubble(rest(l)))


def bubbleSort(l):
  return foldr(l, lambda _, bl: bubble(bl), l)

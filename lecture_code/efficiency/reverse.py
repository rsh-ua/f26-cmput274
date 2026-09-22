from cmput274 import *


def append(elem, l):
  if isEmpty(l):
    return cons(elem, empty())
  return cons(first(l), append(elem, rest(l)))

def reverse(l):
  '''
  reverse produces the reversed version of a LList l

  l       - LList of Any
  returns - LList of Any

  Examples:
    reverse(cons(1,(cons(2,cons(3,empty())))) -> <3,2,1>
  '''
  if isEmpty(l):
    return empty()
  ror = reverse(rest(l))
  v0 = first(l)
  # if l is <v0, v1, ..., vn>
  # then rest(l) is <v1, ..., vn>
  # so reverse(rest(l)) <vn, vn-1, ..., v1>
  # What do I want to do to the list <vn, vn-1, ..., v1>
  # to produce my answer?
  # We want to append v0 onto ror!
  return append(v0, ror)

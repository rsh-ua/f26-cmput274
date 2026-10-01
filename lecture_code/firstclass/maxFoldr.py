from cmput274 import *

def chooseLargest(elem, largestSoFar):
  if elem > largestSoFar:
    return elem
  return largestSoFar

def maxLList(l):
  return foldr(l, chooseLargest, first(l))



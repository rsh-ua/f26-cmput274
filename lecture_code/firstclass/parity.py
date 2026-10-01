from cmput274 import *

def countOne(char, countSoFar):
  if char == "1":
    return 1+countSoFar
  return countSoFar

def parity(bs):
  # returns True if BinaryStr bs has an even number of "1" characters
  # False otherwise
  count = foldr(bs, countOne, 0)
  return count%2 == 0

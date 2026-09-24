from cmput274 import *
import sys

def ascendListHelper(n, sub):
  if sub == 0:
    return cons(n, empty())
  return cons(n-sub, ascendListHelper(n, sub-1))

def ascendList(n):
  '''
  ascendList produces the LList from 0...n in ascending order

  n       - a Nat
  returns - a LList of Nat

  Examples:
    ascendList(3) -> (0, 1, 2, 3)
    ascendList(0) -> (0)
  '''
  return ascendListHelper(n, n)


def main():
  # You can't use these things, only for demonstration
  n = int(sys.argv[1])
  l = ascendList(n)

if __name__ == "__main__":
  main()


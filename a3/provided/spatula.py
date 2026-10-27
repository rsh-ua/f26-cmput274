from cmput274 import *

def flip(l, k):
  '''
  flip returns the result of "flipping" the first k elements of
       the LList l, which is to say it returns the result of
       LList l with the first l elements reversed.

  l       - LList of X
  k       - Nat
  returns - LList of X

  Examples:
    flip(LL(1,2,3,4,5,6), 3) -> LL(3,2,1,4,5,6)
  '''
  def takeN(l, n):
    if n == 0:
      return empty()
    return cons(first(l), takeN(rest(l), n-1))
  def skipN(l, n):
    if n == 0:
      return l
    return skipN(rest(l), n-1)
  return foldr(foldl(takeN(l,k), cons, empty()), cons, skipN(l,k))

def flipSort(l):
  # TODO: Implement this function
  pass


def main():
  # Provided tests are only sanity checks and examples.
  # Make sure to write more of your own tests to verify your work thoroughly!
  testExact("t1", LL(1, 2, 3, 4, 5), flipSort, LL(3, 5, 2, 4, 1))
  runTests()

if __name__ == "__main__":
  main()

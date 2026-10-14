from cmput274 import *

def collectionToIndices(c):
  '''
  collectionToIndices returns for a given collection c of length n
                      a LList of the values from (0,1,...,n-1)

  c       - Any sequence
  returns - a LList of Nat

  Examples:
    collectionToIndices("hello") -> LL(0, 1, 2, 3, 4)
    collectionToIndices(LL(5, 20, 3)) -> LL(0, 1, 2)
  '''
  size = foldr(c, lambda _, total: 1+total, 0)
  return rest(foldr(c, lambda _, l: cons(first(l)-1, l), LL(size-1)))

'''
This problem of wanting a collection of (0,...n-1)
or even wanting a collection of (f(0), f(1),..., f(n-1)
is very common!

Now that we have collectionToIndices we can easily form
the latter by simply mapping f onto the collection of indices

But what if we don't have a collecton that defines n? What if
we just have the number we want n?
'''

def buildList(f, n):
  '''
  buildList produces a mapping of f onto the natural numbers
            [0,n)

  f       - (Nat -> X)
  n       - Nat
  returns - LList of X

  Examples:
    buildList(lambda x: x*2, 5) -> LL(0, 2, 4, 6, 8)
    buildList(lambda x: x%3, 7) -> LL(0, 1, 2, 0, 1, 2, 0)
  '''
  def buildListAcc(f, i, asf):
    if i == 0:
      return cons(f(0), asf)
    return buildListAcc(f, i-1, cons(f(i), asf))
  return buildListAcc(f, n-1, empty())

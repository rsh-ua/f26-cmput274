from cmput274 import *


def fnwhile(p, f):
  '''
  fnwhile returns a unary function which repeatedly calls f (first on the argument of
          unary function, subsequently on the results of f) until the value does not meet
          predicate p

  p      - (X -> bool)
  f      - (X -> X)
  return - (X -> X)
  '''
  def helper(x):
    if not p(x):
      return x
    return helper(f(x))
  return helper

def main():
  # How to use fnwhile to simulate the while loop that sums a llist?
  # Ultimately, this fn can simulate ANY while loop, we just have to get clever
  # about how we encode our loops data into p, f, and our initial argument provided
  # to the returned argument by fnwhile

  # Our while loop that sums a LList had two main pieces of data - the LList itself
  # which tracked our progress, and the integer sum. We need to encode both these
  # pieces of data at each step of our f and predicate. So, the single parameter
  # that f takes will be a tuple of the form (sumSoFar, listLeft)
  predicate = lambda p: not isEmpty(p[1])
  f = lambda p: (p[0]+first(p[1]), rest(p[1]))
  sumLList = lambda l: fnwhile(predicate, f)((0, l))[0]

from cmput274 import *

def reverseParams(f):
  # TODO
  pass


def conjunction(l):
  # TODO
  pass

def repeat(f, n):
  # TODO
  pass


def until(p, f):
  # TODO
  pass


def main():
  # Provided tests are only sanity checks and examples.
  # Make sure to write more of your own tests to verify your work thoroughly!
  reversed1 = reverseParams(lambda x, y: x / y)
  testExact("reverseT1", 0.5, reversed1, 2, 1)
  reversed2 = reverseParams(lambda x, y: x - y)
  testExact("reverseT2", -5, reversed2, 5, 0)

  isEven = lambda x: x % 2 == 0
  isNonNeg = lambda x : x >= 0
  isSmall = lambda x : x < 100
  allAbove = conjunction(LL(isEven, isNonNeg, isSmall))
  testExact("conjunctionT1", False, allAbove, 102)
  testExact("conjunctionT2", False, allAbove, -2)
  testExact("conjunctionT3", False, allAbove, 3)
  testExact("conjunctionT4", True, allAbove, 4)
  testExact("conjunctionT5", True, conjunction(LL(isSmall, isNonNeg)), 3)

  rep1 = repeat(lambda x: x*2-1, 3)
  rep2 = repeat(lambda x: x//2, 5)
  testExact("repeatT1", 17, rep1, 3)
  testExact("repeatT2", 54, rep2, 1735)

  unt1 = until(lambda x: x > 100, lambda x: x*2)

  testExact("untilT1", 192, unt1, 3)

  runTests()

if __name__ == "__main__":
  main()

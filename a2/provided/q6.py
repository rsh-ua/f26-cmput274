from cmput274 import *

def dedup(l):
  # Remove the "pass" line and fill in this function.
  # Don't forget to include your function specification
  # docstring at the beginning of the function!
  pass

def main():
  testExact("basic1", LL(1, 2, 8, 7), dedup, LL(1, 1, 1, 2, 1, 8, 2, 7, 8))
  testExact("basic2", LL(2, 3, 5, 7, 9), dedup, LL(2, 3, 5, 7, 9, 9, 7, 9, 5, 2, 3, 2, 7))
  # Add your own test cases here, before the call to runTests

  runTests()

if __name__ == "__main__":
  main()

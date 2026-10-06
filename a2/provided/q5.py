from cmput274 import *

def hammingDistance(s1, s2):
  # Remove the "pass" line and fill in this function.
  # Don't forget to include your function specification
  # docstring at the beginning of the function!
  pass

def main():
  testExact("basic1", 1, hammingDistance, "axyz", "axzz")
  testExact("basic1", 4, hammingDistance, "abc----", "abc")
  testExact("basic1", 3, hammingDistance, "grey", "hazy")
  # Add your own test cases here, before the call to runTests

  runTests()

if __name__ == "__main__":
  main()

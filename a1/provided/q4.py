from cmput274 import *
<<<<<<< HEAD

def primeHelper(n, i):
  if i == 1:
    return True
  if n%i == 0:
    return False
  return primeHelper(n, i-1)

def isPrime(n):
  from math import ceil, sqrt
  return primeHelper(n, ceil(sqrt(n)))
=======
# The above line should appear at the start of
# all of your CMPUT274 programs

def isPrime(n):
  # Remove the "pass" line and fill in this function.
  # Don't forget to include your function specification
  # docstring at the beginning of the function!
  pass
>>>>>>> ad9d58d178628d3a4cae71b9391c069f2cd407ea


def main():
  testExact("basic1", True, isPrime, 7)
  testExact("basic2", False, isPrime, 91)
<<<<<<< HEAD
  testExact("basic3", False, isPrime, 1000000)
  testExact("basic3", False, isPrime, 10000000)

=======
  # Write your own test cases here as you see fit.
  # You should write many test cases to make yourself
  # confident your solution works before you hand it in!
>>>>>>> ad9d58d178628d3a4cae71b9391c069f2cd407ea
  runTests()

if __name__ == "__main__":
  main()

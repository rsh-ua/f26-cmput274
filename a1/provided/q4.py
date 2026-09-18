from cmput274 import *

def primeHelper(n, i):
  if i == 1:
    return True
  if n%i == 0:
    return False
  return primeHelper(n, i-1)

def isPrime(n):
  from math import ceil, sqrt
  return primeHelper(n, ceil(sqrt(n)))


def main():
  testExact("basic1", True, isPrime, 7)
  testExact("basic2", False, isPrime, 91)
  testExact("basic3", False, isPrime, 1000000)
  testExact("basic3", False, isPrime, 10000000)

  runTests()

if __name__ == "__main__":
  main()

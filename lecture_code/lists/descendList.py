from cmput274 import *
import sys
def descendList(n):
  '''
  descendList produces the LList that contains the
              natural numbers from n to zero in descending order

  n       - a Nat
  returns - a LList of Nat

  Examples:
    descendList(5) -> (5, 4, 3, 2, 1, 0)
    descendList(2) -> (2, 1, 0)
    descendList(0) -> (0)
  '''
  if n == 0:
    return cons(0, empty())
  # Given I have the number n, how do I build the
  # LList of the numbers (n,n-1,...0) with the functions
  # I have over LLists?
  # The only functions I have are empty() and cons
  # cons takes an element and prepends it to an existing LList
  # So the only expression I can write to produce this list
  # is cons(n, (n-1,n-2,...0))
  return cons(n, descendList(n-1))

def main():
  n = int(sys.argv[1])
  l = descendList(n)

if __name__ == "__main__":
  main()

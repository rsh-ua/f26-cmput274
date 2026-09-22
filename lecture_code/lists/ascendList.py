from cmput274 import *
import sys
def append(elem, l):
  '''
  append produces a new LList that is the result of appending elem onto l

  elem    - Any
  l       - a LList of Any
  returns - a LList of Any

  Examples:
    append(5, cons(0, cons(1, empty()))) -> <0,1,5>
  '''
  if isEmpty(l):
    # Appending an element to the empty LList is simply the LList
    # with only that empty (appending to the empty list is the same
    # as prepending)
    return cons(elem, empty())
  # if my llist is not empty then I can't place my element there...
  # so I need to solve a smaller problem...
  # So I /could/ append the element to the rest of the list!
  ror = append(elem, rest(l))
  # Assuming our function works then if l is (v0,v1,...,vn)
  # then append(e,rest(l)) -> (v1,...,vn,e)
  # if I have (v1,...,vn,e) how can I build my answer (v0,v1,...,vn,e)?
  # (v0,v1,...vn,e) is just cons(v0, (v1,v2,...vn,e)), since ror is already
  # that list I just need to cons(v0, ror)!
  return cons(first(l), ror)

def ascendList(n):
  '''
  ascendList produces the LList from 0...n in ascending order

  n       - a Nat
  returns - a LList of Nat

  Examples:
    ascendList(3) -> (0, 1, 2, 3)
    ascendList(0) -> (0)
  '''
  if n == 0:
    return cons(0,empty())
  # n is my current element... need to do something with it
  # I want the LList (0,1,...,n)
  ror = ascendList(n-1)
  # assume our function works then ror is (0,...,n-1)
  # given that list what we need to do is produce a new list
  # that is ror with n added to the /back/ of it - we need to
  # APPEND n as opposed to prepend it.
  return append(n, ror)



def main():
  # You can't use these things, only for demonstration
  n = int(sys.argv[1])
  l = ascendList(n)

if __name__ == "__main__":
  main()


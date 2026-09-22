from cmput274 import *

def reverseHelper(l, asf):
  '''
  reverseHelper takes a LList l and a LList asf that is the answer so far
                of reversing a LList and returns the reversed list.
                if l is <v0,...,vn> and asf is <q0,...,qn>
                we produce <vn,...,v0,q0,...qn>. Semantically asf
                can be thought of as "all the parts of my list I've already
                reversed"

  l       - LList of Any
  asf     - LList of Any
  returns - LList of Any

  Examples:
    reverseHelper(<1,2,3>, <0,-1>) -> <3,2,1,0,-1>
  '''
  if isEmpty(l): # if the list I want to reverse is empty
    # no more work to do
    # if there's no more work to do then my "answer-so-far"
    # is my FINAL answer!
    return asf
  # Our asf we decided was always meant to represent the LList we'd
  # like to prepend to. If it is in the fact the LList we'd like to
  # prepend to how do we build up our answer?
  return reverseHelper(rest(l), cons(first(l), asf))
def reverse(l):
  return reverseHelper(l,empty())



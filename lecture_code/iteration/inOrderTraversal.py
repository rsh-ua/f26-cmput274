from cmput274 import *
'''
A Stack of X is one of
  - emptyStack()
  - push(X, Stack of X)
'''
emptyStack = empty
push = cons
pop = rest
peek = first
stackIsEmpty = isEmpty
append = lambda l, x: foldr(l, cons, LL(x))
'''
A BTree of X is one of
  - ()
  - (X, BTree, BTree)
'''

def inBTToLList(t):
  cStack = push(t, emptyStack()) # Our first "fn call" is on the tree T
  ans = empty()
  while not stackIsEmpty(cStack): # If there are still "stackframes" to execute we must continue
    curTree = peek(cStack) # top our stack is our current stackframe
    cStack = pop(cStack) # Remove our current stack frame for processing
    # If our current tree IS a leaf then processing it just means appending it
    # to our answer!
    if t[1] == () and t[2] == ():
      ans = append(ans, t[0])
    else:
      # if our tree is NOT a leaf, then we must break it down into
      # up to three "recursive calls"
      if t[2] != ():
        cStack = push(t[2], cStack)
      cStack = push((t[0], (), ()), cStack)
      if t[1] != ():
        cStack = push(t[1], cStack)
  return ans

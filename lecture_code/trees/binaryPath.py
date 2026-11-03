from cmput274 import *

# A BinaryTree of X is one of
# - (), the empty tuple
# - (X, BinaryTree, BinaryTree)

def findPath(bt, v):
  '''
  findPath finds the series of directions from the tree rooted at bt
           to the value v within that tree.

  bt       - BinaryTree of X
  v        - x
  Returns  - anyof(None, LList of anyof("left", "right"))

  Examples:
    findPath((5,
                (3,
                  (),
                  (2, (), ())
                ),
                (7,
                  (8, (), ()),
                  (9, (), ())
                )
              ), 2) -> LL("left", "right")
  '''
  if bt == ():
    return None
  if bt[0] == v:
    return empty() # No directions needed! You're home :)
  if bt[1] == () and bt[2] == (): # No children, I'm a leaf but my val is not what we're looking for
    return None # None is the only value of type NoneType. It's purpose is to represent
    # the /absence/ of a value. Should we NOT find a path to the target value then we want
    # to represent /NO PATH/ the ABSENCE of a path. We can't represent our non-existant path
    # as a LList, because every value in our valid LLists is a valid path (the empty LList is
    # the path when we're already at our target)
  lChild = bt[1]
  rChild = bt[2]
  leftRor = findPath(lChild, v)
  if leftRor != None:
    # if leftRor is not none... then it's the path from that child to the target!
    return cons("left", leftRor)
    # my path to the target is to go left to go to my left child
    # and then take whatever their path to the target is!
  rightRor = findPath(rChild, v)
  if rightRor != None:
    # Same logic... my right child's path to the target is rightRor
    # then my path to the target is go right to get to my right child
    # and then follow their path!
    return cons("right", rightRor)
  return None

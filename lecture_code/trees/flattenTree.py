from cmput274 import *

def concat(l1, l2, l3):
  return foldr(l1, cons, foldr(l2, cons, l3))



def flatten1(bt):
  '''
  flatten produces a LList of all the values in the binary tree bt

  bt      - BinaryTree of X
  returns - LList of X
  '''
  if bt == ():
    return empty()
  return concat(LL(bt[0]), flatten(bt[1]), flatten(bt[2]))


def flatten2(bt):
  '''
  flatten produces a LList of all the values in the binary tree bt

  bt      - BinaryTree of X
  returns - LList of X
  '''
  if bt == ():
    return empty()
  return concat(flatten2(bt[1]), LL(bt[0]), flatten2(bt[2]))


def flatten3(bt):
  '''
  flatten produces a LList of all the values in the binary tree bt

  bt      - BinaryTree of X
  returns - LList of X
  '''
  if bt == ():
    return empty()
  val = LL(bt[0])
  lTree = bt[1]
  rTree = bt[2]
  return concat(flatten3(lTree), concat(flatten3(rTree), val))

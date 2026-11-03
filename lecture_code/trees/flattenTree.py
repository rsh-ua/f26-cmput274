from cmput274 import *

def concat(l1, l2):
  return foldr(l1, cons, l2)

def flatten1(bt):
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
  return concat(val, concat(flatten1(lTree), flatten1(rTree)))

def flatten2(bt):
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
  return concat(flatten2(lTree), concat(val, flatten2(rTree)))

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

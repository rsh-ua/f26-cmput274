from cmput274 import *

def sub(x, y, z):
  return x - y - z

def identity(x):
  return x

def preTD(bt):
  if bt == ():
    return 0
  return sub(identity(bt[0]), preTD(bt[1]), preTD(bt[2]))

def inTD(bt):
  if bt == ():
    return 0
  return sub(inTD(bt[1]), bt[0], inTD(bt[2]))

def postTD(bt):
  if bt == ():
    return 0
  return sub(postTD(bt[1]), postTD(bt[2]), bt[0])


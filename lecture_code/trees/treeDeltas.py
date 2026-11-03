from cmput274 import *

def sub(x, y, z):
  return x - y - z

def preTD(bt):
  if bt == ():
    return 0
  return sub(bt[0], bt[1], bt[2])

def inTD(bt):
  if bt == ():
    return 0
  return sub(inTD(bt[1]), bt[0], inTD(bt[2]))

def postTD(bt):
  if bt == ():
    return 0
  return postTD(bt[1]) - postTD(bt[2]) - bt[0]


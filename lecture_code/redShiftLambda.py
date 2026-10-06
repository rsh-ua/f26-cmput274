from cmput274 import *


def redShiftGenerator(sAmt):
  newRed = sAmt+first(p)
  rl = rest(p)
  return lambda p: cons(newRed, rl) if newRed < 255 and newRed > 0 else (cons(255, rl) if newRed >= 255 else cons(0, rl))

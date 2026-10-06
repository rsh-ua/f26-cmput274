from cmput274 import *


def redShiftGenerator(sAmt):
  capper = lambda num : 255 if num > 255 else (0 if num < 0 else num)
  return lambda p: cons(capper(first(p)+sAmt), rest(p))


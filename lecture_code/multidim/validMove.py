
from cmput274 import *

def validMove(world, pPos):
  leftCoord = pPos - 1
  ans = empty()
  if leftCoord >= 0 and world[leftCoord] == 0:
    ans =  cons("left", ans)
  rightCoord = pPos + 1
  if rightCoord < len(world) and world[rightCoord] == 0:
    ans = cons("right", ans)
  return ans

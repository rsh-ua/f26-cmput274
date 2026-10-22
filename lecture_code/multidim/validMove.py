
from cmput274 import *

def validMove(world, pPos):
  '''
  validMove returns a tuple of the strings that represent the directions
            the player in twoDimensionalWarrior can move

  world     - a tuple of anyof(0,1)
  pPos      - a tuple of (Nat, Nat) (x,y)
  returns   - a tuple of str
  ...
  '''
  def isBounded(coord):
    x = coord[0]
    y = coord[1]
    minYCoord = 0
    minXCoord = 0
    yCoordEnd = len(world)
    if y < minYCoord or y >= yCoordEnd:
      return False
    xCoordEnd = len(world[y]) # must know if y is a valid coord before
    # indexing our world with it!
    return x >= minXCoord and x < xCoordEnd
  def isWall(coord):
    x = coord[0]
    y = coord[1]
    return world[y][x] == 1
  leftCoord = (pPos[0]+(-1), pPos[1]+0)
  rightCoord = (pPos[0]+1, pPos[1]+0)
  upCoord = (pPos[0]+0, pPos[1]+(-1))
  downCoord = (pPos[0]+0, pPos[1]+1)
  '''
  ans = ()
  if isBounded(leftCoord) and not isWall(leftCoord):
    ans = ans + ("left",)
  if isBounded(rightCoord) and not isWall(rightCoord):
    ans = ans + ("right",)
  if isBounded(upCoord) and not isWall(upCoord):
    ans = ans + ("up",)
  if isBounded(downCoord) and not isWall(downCoord):
    ans = ans + ("down",)
  # This code worked... but to create it we copied the first
  # condition three more times and simply updated two things
  # in the condition. We changed the coord used and the
  # answer if that coord was valid! So... like with any repetitive
  # task with similarities let's abstract out the differences
  # so we can write it as ONE task with the differences being
  # parameters
  '''
  options = ((leftCoord, "left"),
             (rightCoord, "right"),
             (upCoord, "up"),
             (downCoord, "down"))
  goodPos = lambda pos: isBounded(pos) and not isWall(pos)
  foldF = lambda pair, ans: (pair[1],) + ans if goodPos(pair[0]) else ans
  return foldr(options, foldF, ())

from cmput274 import *

def inBounds(grid, pos):
  xPos = pos[0]
  yPos = pos[1]
  if yPos < 0 or yPos >= len(grid):
    return False
  return xPos >= 0 and xPos < len(grid[yPos])

def adjacentBombs(grid, x, y):
  # a coordDelta will be a tuple of the form (anyOf(-1,0,1), anyOf(-1,0,1))
  allCoords = map(lambda xD: map(lambda yD: (xD+x, yD+y), (-1,0,1)), (-1,0,1))
  concat = lambda l1, l2: foldr(l1, cons, l2)
  flatCoords = foldr(allCoords, lambda l1, ror: concat(l1, ror), empty())
  goodPos = filter(lambda coord: coord != (x,y), flatCoords)
  inBoundPos = filter(lambda coord: inBounds(grid, coord), goodPos)
  bombPos = filter(lambda coord: grid[coord[1]][coord[0]] == "B", inBoundPos)
  return len(bombPos)

def main():
  bigGrid = (
  ("O","O","B","O","O","O","O","B","O","O","O","O","B","O","O","O","O","O","B","O","O","O","B","O","O","O","O","B","O","O","O","O","B","O","O","O","O","B","O","O"),
  ("O","B","O","O","O","B","O","O","O","O","B","O","O","O","B","O","O","O","O","B","O","O","B","O","O","O","B","O","O","O","O","B","O","O","O","B","O","O","O","O"),
  ("O","O","O","B","O","O","O","O","B","O","O","B","O","O","O","O","B","O","O","O","B","O","O","O","O","B","O","O","O","B","O","O","O","O","B","O","O","B","O","O"),
  ("B","O","O","O","O","B","O","O","O","B","O","O","O","O","B","O","O","B","O","O","O","O","B","O","O","O","B","O","O","B","O","O","O","O","B","O","O","O","O","B"),
  ("O","O","B","O","O","O","B","O","O","O","O","B","O","O","B","O","O","O","O","B","O","O","O","B","O","O","O","O","B","O","O","B","O","O","O","B","O","O","O","O"),
  ("O","B","O","O","B","O","O","O","O","B","O","O","O","B","O","O","O","O","B","O","O","B","O","O","O","O","B","O","O","O","B","O","O","O","O","B","O","O","B","O"),
  ("O","O","O","B","O","O","B","O","O","O","O","B","O","O","O","B","O","O","O","O","B","O","O","O","B","O","O","B","O","O","O","O","B","O","O","O","B","O","O","O"),
  ("B","O","O","O","O","B","O","O","B","O","O","O","O","B","O","O","O","B","O","O","O","B","O","O","O","O","B","O","O","B","O","O","O","B","O","O","O","O","B","O"),
  ("O","O","B","O","O","O","O","B","O","O","B","O","O","O","O","B","O","O","B","O","O","O","O","B","O","O","O","B","O","O","B","O","O","O","O","B","O","O","B","O"),
  ("O","B","O","O","O","B","O","O","O","O","B","O","O","B","O","O","O","O","B","O","O","O","B","O","O","O","O","B","O","O","O","O","B","O","O","B","O","O","O","O"),
  ("O","O","O","B","O","O","O","O","B","O","O","O","B","O","O","B","O","O","O","O","B","O","O","B","O","O","O","O","B","O","O","O","B","O","O","O","O","B","O","O"),
  ("B","O","O","O","B","O","O","O","O","B","O","O","B","O","O","O","O","B","O","O","O","B","O","O","O","B","O","O","O","O","B","O","O","B","O","O","O","O","B","O"),
  ("O","O","B","O","O","O","B","O","O","B","O","O","O","O","B","O","O","O","B","O","O","O","O","B","O","O","B","O","O","O","B","O","O","O","O","B","O","O","O","B"),
  ("O","B","O","O","O","O","B","O","O","O","B","O","O","O","O","B","O","O","O","B","O","O","B","O","O","O","O","B","O","O","O","B","O","O","O","O","B","O","O","O"),
  ("O","O","O","B","O","O","O","B","O","O","O","O","B","O","O","B","O","O","O","O","B","O","O","O","B","O","O","O","O","B","O","O","B","O","O","O","B","O","O","B"),
  ("B","O","O","O","O","B","O","O","O","B","O","O","O","O","B","O","O","B","O","O","O","O","B","O","O","O","B","O","O","B","O","O","O","O","B","O","O","O","B","O"),
  ("O","O","B","O","O","O","O","B","O","O","O","B","O","O","O","O","B","O","O","O","B","O","O","B","O","O","O","O","B","O","O","O","B","O","O","O","O","B","O","O"),
  ("O","B","O","O","B","O","O","O","O","B","O","O","B","O","O","O","O","B","O","O","O","B","O","O","O","B","O","O","B","O","O","O","O","B","O","O","O","B","O","O"),
  ("O","O","O","B","O","O","B","O","O","O","O","B","O","O","B","O","O","O","O","B","O","O","O","B","O","O","O","O","B","O","O","B","O","O","O","B","O","O","O","O"),
  ("B","O","O","O","B","O","O","O","B","O","O","O","O","B","O","O","O","B","O","O","B","O","O","O","O","B","O","O","O","B","O","O","O","O","B","O","O","B","O","O"),
  ("O","O","B","O","O","O","O","B","O","O","B","O","O","O","O","B","O","O","O","O","B","O","O","B","O","O","O","B","O","O","B","O","O","O","O","B","O","O","B","O"),
  ("O","B","O","O","O","B","O","O","O","O","B","O","O","B","O","O","O","O","B","O","O","O","B","O","O","O","B","O","O","O","O","B","O","O","O","B","O","O","O","O"),
  ("O","O","O","B","O","O","O","O","B","O","O","O","B","O","O","B","O","O","O","O","B","O","O","O","B","O","O","O","O","B","O","O","B","O","O","O","B","O","O","O"),
  ("B","O","O","O","O","B","O","O","B","O","O","O","O","B","O","O","O","B","O","O","O","B","O","O","O","O","B","O","O","B","O","O","O","B","O","O","O","O","B","O"),
  ("O","O","B","O","O","O","B","O","O","O","B","O","O","O","O","B","O","O","B","O","O","O","O","B","O","O","O","B","O","O","B","O","O","O","O","B","O","O","B","O"),
  ("O","B","O","O","B","O","O","O","O","B","O","O","O","B","O","O","O","O","B","O","O","B","O","O","O","O","B","O","O","O","B","O","O","O","O","B","O","O","O","B"),
  ("O","O","O","B","O","O","B","O","O","O","O","B","O","O","O","B","O","O","O","O","B","O","O","O","B","O","O","B","O","O","O","O","B","O","O","O","B","O","O","O"),
  ("B","O","O","O","O","B","O","O","O","B","O","O","B","O","O","O","O","B","O","O","O","B","O","O","O","B","O","O","O","O","B","O","O","B","O","O","O","O","B","O"),
  ("O","O","B","O","O","O","O","B","O","O","O","B","O","O","B","O","O","O","O","B","O","O","O","B","O","O","O","O","B","O","O","B","O","O","O","B","O","O","O","O"),
  ("O","B","O","O","O","B","O","O","O","O","B","O","O","O","O","B","O","O","B","O","O","O","B","O","O","O","B","O","O","O","O","B","O","O","O","O","B","O","O","B"))
  g = (("B", "O", "B"),
       ("O", "B", "O"),
       ("B", "B", "B"))
  testExact("t1", 4, adjacentBombs, g, 0, 1)
  testExact("t2", 5, adjacentBombs, g, 1, 1)
  testExact("t4", 2, adjacentBombs, g, 2, 2)
  testExact("t3", 3, adjacentBombs, bigGrid, 7, 13)
  runTests()


if __name__ == "__main__":
  main()

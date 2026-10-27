from cmput274 import *

# A Square is a 2-tuple (Nat, Nat)
#   which represents the row an column numbers
#   of an individual square of a deficient board.

# A Region is a 2-tuple (Square, Nat)
#   where the Square is the top left square of this square
#   region and the Nat represents the length of the sides
#   and the Nat is always a Power of 2

# A Tromino is a 3-tuple (Square, Square, Square)
#   in which each Square is unique, and adjacent to one
#   other square in the 3-tuple.

# A Tiling is a LList of Trominoes


def tileDeficientBoard(board, hole):
  # TODO
  pass


def main():
  # Provided tests are only sanity checks and examples.
  # Make sure to write more of your own tests to verify your work thoroughly!

  # Functions used in these test cases are not freely available for use outside of these test
  # cases (e.g. you can't use sorted in other places just because it appears here, but may use
  # it to write more of these test cases)
  def compareSquares(sq1, sq2):
    # Used to sort the squares inside a tromino
    return sq1[0] < sq2[0] or (sq1[0] == sq2[0] and sq1[1] < sq2[1])
  def compareTrominos(t1, t2):
    # Used to compare trominos inside a tiling
    if compareSquares(t1[0], t2[0]):
      return True
    if not compareSquares(t2[0], t1[0]) and compareSquares(t1[1], t2[1]):
      return True
    if not compareSquares(t2[0], t1[0]) and not compareSquares(t2[1], t1[1]) and compareSquares(t1[2], t2[2]):
      return True
    return False 
  from functools import cmp_to_key
  tromKey=cmp_to_key(compareTrominos)

  board4x4 = ((0, 0), 4)
  hole4x4 = (1,2)
  expected4x4 = (((1,1),(2,1),(2,2)), ((0,0),(0,1),(1,0)), ((0,2),(0,3),(1,3)), ((2,0),(3,0),(3,1)), ((2,3),(3,2),(3,3)))
  apply4x4 = lambda hole: sorted(tileDeficientBoard(board4x4, hole), key=tromKey)
  testExact("t1", sorted(expected4x4, key=tromKey), apply4x4, hole4x4)

  board2x2 = ((0, 0), 2)

  apply2x2 = lambda hole: sorted(tileDeficientBoard(board2x2, hole), key=tromKey)
  expected2x2_hole00 = (((0,1),(1,0),(1,1)),)
  expected2x2_hole11 = (((0,0),(0,1),(1,0)),)
  testExact("t2", sorted(expected2x2_hole00, key=tromKey), apply2x2, (0,0))
  testExact("t3", sorted(expected2x2_hole11, key=tromKey), apply2x2, (1,1))

  runTests()



if __name__ == "__main__":
  main()
from cmput274 import *

def displayWorld(world, pPos):
  '''
  displayWorld returns a string that represents the display of the
               game of one dimensional warrior described by world
               and pPos
  world     - Tuple of anyof(0,1)
  pPos      - A Nat
  Returns   - A Str

  Examples:
    displayWorld((0,1,0,0,0,1,0,0,0), 3) -> "_|_Ÿ_|___"
  '''
  # We need to find a function that transforms some data
  # into the string we want
  # We can map values in our world to characters, BUT
  # that doesn't tell us about the player character.
  # For the player we can only map coordinate to that.
  # So we need to find not only a way to map coordinate to
  # the player's character but the character for other tiles
  # as well. Thankfully, if we can map values in our collection
  # to their corresponding characters (we can) and we can map
  # coordinates to their values in our world (we can its indexing)
  # then we can map coordinates to characters!
  natToChar = lambda n: "_" if n == 0 else "|"
  indices = buildList(lambda x:x, len(world))
  indToChar = lambda i: "Ÿ" if pPos == i else natToChar(world[i])
  return foldr(indices, lambda i, ror: indToChar(i) + ror, "")


def main():
  sampleWorld = (0,1,0,0,0,1,0,0,0)
  playerPosition = 3 # Positions are discussed in terms of coordinates.
  # Since have a one-dimensional world our coordinate is just 1 Nat,
  # the index into our world data collection
  testExact("t1", "_|_Ÿ_|___", displayWorld, sampleWorld, playerPosition)
  testExact("t2", "Ÿ|___|___", displayWorld, sampleWorld, 0)
  runTests()


if __name__ == "__main__":
  main()


def logfloor(n):
  '''
  logfloor of n returns the floor of the base-10 log of n

  n - an natural number greater than 0
  returns - a natural number

  Examples:
    logfloor(1) -> 0
    logfloor(735) -> 2
    logfloor(12345) -> 4
  '''
  assert n > 0
  if n < 10:
    return 0
  ror = logfloor(n//10)
  return 1 + ror

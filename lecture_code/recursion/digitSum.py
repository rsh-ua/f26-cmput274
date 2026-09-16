
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


def digitSum(n):
  '''
  digitSum returns the sum of the digits of n

  n       - a natural number
  returns - a natural number

  Examples:
    digitSum(735) -> 15
    digitSum(10000) -> 1
  '''
  if n < 10:
    return n
  currentDigit = n//(10**logfloor(n))
  # To step closer to our base case we now need to take
  # that digit off our leftmost digit of our number...
  nextNumber = n - currentDigit*10**logfloor(n)
  ror = digitSum(nextNumber)
  return currentDigit + ror


def digitSum2(n):
  if n < 10:
    return n
  return n%10 + digitSum2(n//10)

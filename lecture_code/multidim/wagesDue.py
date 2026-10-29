from cmput274 import *

# A PayrollItem is a:
#   - cons(str, LList of int)

# A PayrollList is a:
#   - LList of PayrollItem

def payrollItemToWages(pri):
  '''
  pri     - a PayrollItem
  returns - LL(str, float)
  '''
  # LL("str", 4, 3, 2, 10) -> LL("str", (4+3+2+10)*22.50)
  name = first(pri)
  wages = foldr(rest(pri), lambda x, y: x + y, 0)*22.5
  return LL(name, wages)

def wagesDue(prl):
  return map(payrollItemToWages, prl)

def main():
  prl = LL(LL("Erik", 5, 8, 4, 7), LL("Ashley", 6, 2), LL("Stefan", 2, 2, 2, 2, 2, 2, 2))
  res = LL(LL("Erik", 540.0), LL("Ashley", 180.0),LL("Stefan", 315.0))
  testExact("t1", res, wagesDue, prl)
  runTests()
if __name__ == "__main__":
  main()

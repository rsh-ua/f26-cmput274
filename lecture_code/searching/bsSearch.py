from cmput274 import TCO

def bsContains(v, t):
  def bsHelper(lo, hi):
    if lo > hi:
      return False
    mid = lo + (hi-lo)//2
    if t[mid] > v:
      return bsHelper(lo, mid-1)
    if t[mid] < v:
      return bsHelper(mid+1, hi)
    return True
  return bsHelper(0, len(t)-1)

@TCO
def searchHelper(i, v, t):
  if i >= len(t):
    return False
  if t[i] == v:
    return True
  return searchHelper(i+1, v, t)

def linearSearch(v, t):
  return searchHelper(0, v, t)

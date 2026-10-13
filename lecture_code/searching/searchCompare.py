'''
All code used in this file was for demonstration purposes only.

It includes many topics we have not discussed yet and just becasue they appear here
does not mean you may us them!
'''
from random import randint
import sys
from bsSearch import bsContains, linearSearch

def timeTrial(v, t, search):
  from time import time
  start = time()
  search(v, t)
  end = time()
  return end-start

def timeTrials(v, t, search, n):
  if n == 0:
    return 0
  return timeTrial(v, t, search) + timeTrials(v, t, search, n-1)


def main():
  t = (0,)*100000000
  t = tuple(map(lambda x: randint(-2000000000,2000000000), t))
  v = 2000000001
  n = int(sys.argv[1])
  print("Finished generation. Now beginning time trials of searchs.")
  bsSearchT = timeTrials(v, t, bsContains, n)
  lSearchT = timeTrials(v, t, linearSearch, n)
  print(f"Binary search took {bsSearchT:e}s total over {n} trials and an average of {bsSearchT/n:e} per run")
  print(f"Linear search took {lSearchT:e}s total over {n} trials and an average of {lSearchT/n:e} per run")

if __name__ == "__main__":
  main()

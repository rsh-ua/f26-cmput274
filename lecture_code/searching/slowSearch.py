from bsSearch import *
import sys

if __name__ == "__main__":
  sys.setrecursionlimit(200000000)
  f = open("bunchONumbers.txt", "r")
  txt = f.read()
  f.close()
  t = tuple(map(int, txt.strip().split()))
  v = 65535
  ret = linearSearch(v, t)

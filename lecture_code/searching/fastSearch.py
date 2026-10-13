from bsSearch import *


if __name__ == "__main__":
  f = open("bunchONumbers.txt", "r")
  txt = f.read()
  f.close()
  t = tuple(map(int, txt.strip().split()))
  v = 65535
  ret = bsContains(v, t)

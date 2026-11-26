from cmput274 import *
import time

def printSlowly(letter, times):
  # could also use for i in range(times):
  for i in buildList(lambda x: x, times):
    print(letter, end="\n")
    time.sleep(3)

def main():
  printSlowly("x", 10)

if __name__ == "__main__":
  main()

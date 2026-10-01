from cmput274 import *
from math import floor
import sys

'''
A ColorValue (CV) is
  - An int in range [0,255]

A Pixel is a
  - LL(CV, CV, CV)
'''

def specialTransformation(p):
  R = first(p)
  G = first(rest(p))
  B = first(rest(rest(p)))
  newRed =   0.393*R + 0.769*G + 0.189*B
  newGreen = 0.349*R + 0.686*G + 0.168*B
  newBlue =  0.272*R + 0.534*G + 0.131*B
  return map(floor, map(snapTo255, LL(newRed, newGreen, newBlue)))

def redShiftHelper(p, sAmt):
  newRed = first(p) + sAmt
  if newRed > 255:
    return cons(255, rest(p))
  if newRed < 0:
    return cons(0, rest(p))
  return cons(newRed, rest(p))

def redShiftGenerator(sAmt):
  '''
  redShiftGenerator produces a unary function that takes a single Pixel parameter
                    and shifts its red colour components by a particular shift amount

  sAmt      - int
  returns   - (Pixel -> Pixel)

  Examples:
    redShiftGenerator(50) -> fn that takes a pixel and adds 50 to its red component
    redShiftGenerator(50)(LL(20, 30, 70) -> LL(70, 30, 70)
  '''
  return lambda p: redShiftHelper(p, sAmt)

def snapTo255(n):
  if n > 255:
    return 255
  return n

def snapTo0(n):
  if n < 0:
    return 0
  return n

def genShiftHelper(p, r, g, b):
  newRed = first(p) + r
  newGreen = first(rest(p)) + g
  newBlue = first(rest(rest(p))) + b
  newPixel = LL(newRed, newGreen, newBlue)
  return map(snapTo0, map(snapTo255, newPixel))

def genShiftGenerator(r, g, b):
  return lambda p: genShiftHelper(p, r, g, b)

def redShift(pixel):
  newRed = first(pixel)+30
  if newRed > 255:
    return cons(255, rest(pixel))
  return cons(newRed, rest(pixel))

def redderShift(pixel):
  newRed = first(pixel)+65
  if newRed > 255:
    return cons(255, rest(pixel))
  return cons(newRed, rest(pixel))

def redShiftImage(img):
  '''
  redShiftImage applies our redshift transformation to an image

  img     - LList of Pixels
  returns - LList of Pixels
  '''
  return map(redShift, img)

def redderShiftImage(img):
  return map(redderShift, img)
# Note just because things are used in this file does not mean you may use them.

def readPPM(f):
  fobj = open(fname, "r")
  header = fobj.readline()
  w, l = map(int, fobj.readline().strip().split())
  w = int(w)
  l = int(l)
  colorMax = fobj.readline()
  data = fobj.read().strip().split()
  fobj.close()
  imgData = buildList(lambda x: LL(int(data[x*3]), int(data[x*3+1]), int(data[x*3+2])), w*l)
  return w, l, imgData

def writePPM(w, l, data):
  print("P3")
  print(f"{w} {l}")
  print("255")
  map(lambda t: print(f"{first(t)} {first(rest(t))} {first(rest(rest(t)))} "), foldl(data, cons, empty()))

if __name__ == "__main__":
  fname = sys.argv[1]
  w, l, data = readPPM(fname)
  writePPM(w, l, map(specialTransformation, foldl(data, cons, empty())))

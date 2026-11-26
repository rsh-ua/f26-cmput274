from cmput274 import *

def produceBanner(msg, borderChar):
  '''
  produceBanner produces a string which represents a banner
                of borderchar that encloses the given mesage

  msg        - a str
  borderChar - a str, len(borderChar) == 1
  returns    - a str

  Side Effects: None

  Examples:
    produceBanner("Hello World", "-")
      -> "---------------\n- Hello World -\n---------------\n"
  '''
  borderLen = len(msg)+4
  top = borderChar*borderLen + "\n"
  mid = borderChar + " " + msg + " " + borderChar + "\n"
  bottom = borderChar*borderLen + "\n"
  return top+mid+bottom

def displayBanner(msg, borderChar):
  '''
  displayBanner prints to the screen a banner that contains the given
                message within a border made up of borderChar

  msg        - a Str
  borderChar - a single-character Str
  returns    - None

  Side Effects: prints to the screen

  Examples:
      ω is currently "boo"
    displayBanner("Hello World", "-") -> None
      Side Effect: ω becomes "boo---------------\n- Hello World -\n---------------\n"
  '''
  borderLen = len(msg) + 4
  print(borderChar*borderLen)
  print(borderChar + " " + msg + " " + borderChar)
  print(borderChar*borderLen)


def splitStr(msg):
  '''
  splitStr splits up a string on the newLine character producing a LList
           of strings. i.e. if msg is of the form s1\ns2\n...sn\n
           splitStr produces the LList <s1, s2, ..., sn>

  msg     - a str
  returns - LList of str

  Side Effects: None

  Examples:
    splitStr("hello\nabc") -> <"hello", "abc">
    splitStr("hello\n") -> <"hello", "">
    splitStr("\n") -> <"", "">
    splitStr("hello") -> <"hello">
    splitStr("") -> <"">
  '''
  def newLineIndex(msg, curIndex):
    if curIndex == len(msg):
      return curIndex
    if msg[curIndex] == "\n":
      return curIndex
    return newLineIndex(msg, curIndex + 1)
  endCur = newLineIndex(msg, 0)
  curStr = msg[0:endCur]
  if endCur == len(msg):
    return LL(curStr)
  return cons(curStr, splitStr(msg[endCur+1:]))


def displayBanner2(msg, borderStr):
  msgs = splitStr(msg)
  msgs = filter(lambda x: x!="", msgs)
  longestLen = foldr(msgs, lambda x, ror: len(x) if len(x) > ror else ror, 0)
  borderLen = longestLen + 2 + 2*len(borderStr)
  fullBorders = borderLen//len(borderStr)
  rem = borderLen%len(borderStr)
  b = borderStr*fullBorders+borderStr[0:rem]
  print(b)
  for s in msgs:
    padding = (longestLen-len(s))//2
    outS = " "*padding + s + " "*padding + (" " if (longestLen-len(s))%2==1 else "")
    print(borderStr, outS, borderStr)
  print(b)


def main():
  print("boo", end="")
  displayBanner("Hello World", "-")
  print(produceBanner("Hello World", "-"))

if __name__ == "__main__":
  main()

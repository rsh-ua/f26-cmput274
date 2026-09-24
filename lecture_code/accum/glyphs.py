from cmput274 import *


def isOpenGlyph(c):
  # returns true if  char c is an opening glyph
  return c == "{" or c == "[" or c == "("

def isCloseGlyph(c):
  return c == "}" or c == "]" or c == ")"


def matchingGlyphs(open, close):
  '''
  matchingGlyphs returns True if the opening glyph matches the closing glyph

  open    - one of "(", "[", or "{"
  close   - one of ")", "]", or "}"
  returns - bool

  Examples:
    matchingGlyphs("(", "}") -> False
    matchingGlyphs("[", "]") -> True
  '''
  if open == "(" and close == ")":
    return True
  if open == "{" and close == "}":
    return True
  if open == "[" and close == "]":
    return True
  return False

def balancedGlyphsAcc(s, open):
  '''
  balancedGlyphsAcc takes a string to process s and a LList of open glyphs open
                    and returns True if s is balanced assuming the glyphs in open
                    have already previously been opened in the order given

  s       - str
  open    - LList of Char
  returns - bool

  Examples:
    balancedGlyphsAcc(")]z}[hello]", cons("(", cons("[", cons("{", empty()))) -> True
  '''
  if s == "":
    # if the string is empty we've reached our base case. The string is only
    # balanced if we reached this with no remaining open glyphs!
    return isEmpty(open)
  c0 = s[0]
  if isOpenGlyph(c0):
    # If I see an opening glyph... all I did was add it to my notebook of
    # open glyphs and continue looking at the rest of the string! So I do so
    # here too!
    return balancedGlyphsAcc(s[1:], cons(c0, open))
  if isCloseGlyph(c0):
    lastOpen = first(open)
    matched = matchingGlyphs(lastOpen, c0)
    if matched:
      # if these match then we can "close" our most recent open glyph
      # and continue looking at the string
      return balancedGlyphsAcc(s[1:], rest(open))
    else:
      # If the last seen opening glyph doesn't match this closing glyph
      # then the order of glyphs is wrong! Not balanced.
      return False
  # If the glyph is not an opening glyph or a closing glyph
  # simply ignore it and move on!
  return balancedGlyphsAcc(s[1:], open)
def balancedGlyphs(s):
  '''
  balancedGlyphs returns True if all of the parentheses
                 brackets, and braces are balanced in string S
                 and False otherwise

  s       - str
  returns - bool

  Examples:
    balancedGlyphs('{[xt(y)]z}[hello]') -> True
    balancedGlyphs('{[(]})') -> False
    balancedGlyphs('[Hey there :)]') -> False
    balancedGlyphs('((())') -> False
  '''
  return balancedGlyphsAcc(s, empty())


def main():
  testExact("openingGlyph", True, isOpenGlyph, "(")
  testExact("closingNotOpenGlyph", False, isOpenGlyph, ")")
  testExact("non-importantGlyph", False, isOpenGlyph, "k")
  testExact("isOpenGlyph('t')", False, isOpenGlyph, "t")
  testExact("isBalanced", True, balancedGlyphs, '{[xt(y)]z}[hello]')
  testExact("wrongOrder", False, balancedGlyphs, '{[(]})')
  testExact("closeNoOpen", False, balancedGlyphs, '[Hey there :)]')
  testExact("openNoClose", False, balancedGlyphs, '((())')
  runTests()

if __name__ == "__main__":
  main()

from cmput274 import *

def isEnclosingGlyph(c):
  return c == "{" or c == "}" or c == "[" or c == "]" or c == "(" or c == ")"


def isOpeningGlyph(c):
  return c == "{" or c == "[" or c == "("

def matchingOpeningGlyph(c):
  # takes a closing glyph and returns the matching opening glyph
  if c == "}":
    return "{"
  if c == "]":
    return "["
  if c == ")":
    return "("

def balancedGlyphs(s):
  '''
  balancedGlyphs produces True if the enclosing glyphs (parentheses,
                 braces, and brackets) are balanced and False otherwise

  s        - str
  Returns  - bool

  Examples:
    balancedGlyphs("(gafe[awfe{ femaf}woo) done]") -> False
    balancedGlyphs("([{}])") -> True
  '''
  i = 0
  openedGlyphs = empty()
  while i < len(s):
    c = s[i]
    if isEnclosingGlyph(c):
      if isOpeningGlyph(c):
        openedGlyphs = cons(c, openedGlyphs)
      else:
        if isEmpty(openedGlyphs):
          return False
        if matchingOpeningGlyph(c) == first(openedGlyphs):
          openedGlyphs = rest(openedGlyphs)
        else:
          return False
    i = i + 1
  '''
  for c in s:
    if isEnclosingGlyph(c):
      if isOpeningGlyph(c):
        openedGlyphs = cons(c, openedGlyphs)
      else:
        if isEmpty(openedGlyphs):
          return False
        if matchingOpeningGlyph(c) == first(openedGlyphs):
          openedGlyphs = rest(openedGlyphs)
        else:
          return False
  '''
  return isEmpty(openedGlyphs)

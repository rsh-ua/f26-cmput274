
def strlen(s):
  '''
  strlen is a function that returns the length of a string

  s       - a str
  returns - an integer

  Examples:
    strlen("abc") -> 3
    strlen("hello there") -> 11
  '''
  if s == "":
    return 0
  ror = strlen(s[1:])
  return 1 + ror

def streq(s1, s2):
  '''
  streq returns True if s1 == s2 false otherwise

  s1      - a str
  s2      - a str
  returns - a bool

  Examples:
    streq("hello", "Hello") -> False
    streq("abc", "abc") -> True
  '''
  if strlen(s1) == 0 and strlen(s2) == 0:
    return True
  if strlen(s1) != strlen(s2):
    return False
  char1 = s1[0]
  char2 = s2[0]
  ror = streq(s1[1:], s2[1:])
  # ror will be true if the rest of s1 and s2 are
  # equivalent, false otherwise.
  # So how do I process my current characters and
  # combine my result?
  return char1 == char2 and ror

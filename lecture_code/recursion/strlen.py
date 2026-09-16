
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

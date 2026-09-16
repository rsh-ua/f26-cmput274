def convertChar(c):
  '''
  convertChar takes a single character string and converts it
              into the leetspeak equivalent of that character

  c       - a single character string
  returns - a single character string

  Examples:
    convertChar("a") -> "4"
    convertChar("x") -> "x"
  '''
  if c == "e" or c == "E":
    return "3"
  if c == "A" or c == "a":
    return "4"
  if c == "t" or c == "T":
    return "7"
  if c == "l" or c == "L":
    return "1"
  if c == "S" or c == "s":
    return "5"
  if c == "O" or c == "o":
    return "0"
  return c


def leetSpeak(s):
  '''
  leetSpeak converts a string into the leetspeak equivalent

  s       - a string
  returns - a string

  Examples:
    leetSpeak("leetspeak") -> "13375p34k"
    leetSpeak("hacker") -> "h4ckz0r"
    leetSpeak("awplord) -> "4wp10rd"
  '''
  if s == "":
    return ""
  if s == "er":
    return "z0r"
  currentChar = s[0]
  ror = leetSpeak(s[1:])
  # When writing recursive solutions the beauty of recursion is that
  # it simplifies our problem solving by solving a simpler case.
  # We must operate under the assumption that our function specification is
  # correct and our function works. That means, we should assume that
  # leetSpeak(s[1:]), our recursive result, is CORRECT! i.e. ror is now
  # the result of converting the entirety of the string except for the
  # first character into leet speak. So now our problem becomes much simpler:
  # How do I take the first character a non-leetspeak string and the leetspeak
  # version of the rest of the string and produce the leetspeak version of the
  # string?
  # Convert the first character and prepend it to the leetspeak version of
  # the rest of the string!
  return convertChar(currentChar) + ror



# Based on a student question we now write a version that
# converts EVERY occurrence of er to z0r
def badLeetSpeak(s):
  if s == "":
    return ""
  if s[0:2] == "er":
    return "z0r" + badLeetSpeak(s[2:])
  return convertChar(s[0]) + badLeetSpeak(s[1:])

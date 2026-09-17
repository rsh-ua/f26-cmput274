from cmput274 import *

def digitToNumber(c):
  return ord(c) - ord("0")


def strToNum(s):
  '''
  strToNum converts a two-digit string into the corresponding integer

  s       - a string that comprises only two digits
  returns - an integer

  Examples:
    strToNum("95") -> 95
    strToNum("06") -> 6
  '''
  return digitToNumber(s[0])*10 + digitToNumber(s[1])


def timeStrToMinutes(s):
  '''
  timeStrToMinutes converts a time string of the format "HH:MM"
                   into a number of minutes since midnight

  s       - a time string of format "HH:MM"
  returns - integer

  Examples:
    timeStrToMinutes("07:35") -> 455
    timeStrToMinutes("21:03") -> 1263
  '''
  hourStr = s[0:2]
  minStr = s[3:]
  return strToNum(hourStr)*60 + strToNum(minStr)

'''
A TimeStr is a string of the form:
 * "HH:MM"

Where H and M are digits (not necessarily the same)
'''

def timeToEnter(lot, dur):
  '''
  timeToEnter takes a list of pairs of exit/reentry times and
              a duration of minutes necessary to set up a surprise party
              and finds the first occurrence of a time in which the individual
              is out of the house at least dur minutes.

  lot     - A list of TimeStr
  dur     - An integer representing a number of minutes
  returns - A TimeStr if a valid time is found
              False if no such time exists.
  '''
  if isEmpty(lot):
    return False
  exitTime = first(lot)
  returnTime = first(rest(lot))
  if timeStrToMinutes(returnTime) - timeStrToMinutes(exitTime) >= dur:
    return exitTime
  ror = timeToEnter(rest(rest(lot)), dur)

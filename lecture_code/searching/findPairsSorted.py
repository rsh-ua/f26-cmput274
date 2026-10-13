from cmput274 import *

def findPairsSorted(tar, t):
  def fpHelper(start, end):
    if start > end:
      return empty()
    if t[start] + t[end] == tar:
      # if t[start]+t[end] is my target, then add that pair to my answer
      # and remove BOTH start and end from my search space because
      # I have no duplicates (t is in increasing order) and I've already the
      # pair for each of those, so they can't have another pair in my collection
      return cons(LL(t[start], t[end]), fpHelper(start+1, end-1))
    if t[start] + t[end] > tar:
      # if the smallest value in my search space (t[start] because increasing order)
      # summed with the largest value in my search space (t[end] for same reason)
      # is larger than my target... then there's no possible other value in my collection
      # that I could add to my largest value to get a smaller answer (because I already
      # tried my smallest value). SO, my largest value is useless!
      return fpHelper(start, end-1)
    if t[start] + t[end] < tar: #could omit this if due to the mutual exclusivity of the prior conditions
      # if the smallest value in my search space summed with my largest value is still
      # SMALLER than my target, then no other value in my collection added to my smallest
      # value will be any bigger, so my smallest value is useless.
      return fpHelper(start+1, end)
  return fpHelper(0, len(t)-1)

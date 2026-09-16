from math import ceil

def attendance(n):
  if n == 1:
    return 156
  if n > 1:
    return ceil(0.95*attendance(n-1))

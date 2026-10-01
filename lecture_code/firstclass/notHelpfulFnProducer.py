from cmput274 import *

def foo(x):
  return x+3


def produceFoo(y):
  # produceFoo completely ignores its parameter and just returns the function foo
  # because that is the only way we know to specify a function... this is not helpful
  # calling produceFoo is the same as just writing foo...
  return foo

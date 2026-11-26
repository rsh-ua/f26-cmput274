def foo(x):
  fooVar = x*3
  return bar(x*15)

def bar(z):
  result = z*x + fooVar
  return result


def foo2(x):
  def bar2(z):
    result = z*x + fooVar
    return result
  fooVar = x*3
  return bar2(x*15)

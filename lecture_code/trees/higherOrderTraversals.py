from cmput274 import *

def concat(l1, l2, l3):
  return foldr(l1, cons, foldr(l2, cons, l3))


'''
A BinaryTree of X is one of
  - ()
  - (X, BinaryTree of X, BinaryTree of X)

'''
# The following function is based on the data definition above
def preOrderTraversal(bt, comb, f, base):
  '''
  preOrderTraversal performs a pre-order traversal of bt mapping f onto each element and
                    combining the results with comb, producing base when reaching the empty tree.

  bt      - BinaryTree of X
  comb    - (Y Z Z -> Z)
  f       - (X -> Y)
  base    - Z
  returns - Z

  Examples:
    t = (5,
            (3, (7, (), ()), ()),
            (9, (2, (), ()), ()))
    preOrderTraversal(t, lambda v, rorl, rorr: v-rorl-rorr, lambda x: x, 0) -> 2
    preOrderTraversal(t, concat, lambda x: LL(x), empty()) -> <5, 3, 7, 9, 2>
  '''
  if bt == ():
    return base
  return comb(f(bt[0]), preOrderTraversal(bt[1], comb, f, base), preOrderTraversal(bt[2], comb, f, base))


'''
A BinaryTree of X is one of (Constraint based on our implementation, X cannot be a tuple)
  - (X, (), ())
  - (X, BinaryTree Of X, ())
  - (X, (), BinaryTree of X)
  - (X, BinaryTree of X, BinaryTree of X)
'''


# This function is derived from the preceding data defn
def preOrderTraversal2(bt, comb, f, base):
  '''
  preOrderTraversal performs a pre-order traversal of bt mapping f onto each element and
                    combining the results with comb, producing base when reaching the empty tree.

  bt      - BinaryTree of X
  comb    - (Y Y Y -> Y)
  f       - (X -> Y)
  returns - Y

  Examples:
    t = (5,
            (3, (7, (), ()), ()),
            (9, (2, (), ()), ()))
    preOrderTraversal(t, lambda v, rorl, rorr: v-rorl-rorr, lambda x: x) -> 2
    preOrderTraversal(t, concat, lambda x: LL(x)) -> <5, 3, 7, 9, 2>
  '''
  if bt[1] == () and bt[2] == ():
    return f(bt[0]) # Could choose to do comb(f(bt[0]), base, base) but thats just back to the above defn!
  if bt[1] != () and bt[2] == ():
    return comb(f(bt[0]), preOrderTraversal2(bt[1], comb, f, base), base)
  if bt[1] == () and bt[2] != ():
    return comb(f(bt[0]), base, preOrderTraversal2(bt[2], comb, f, base))
  return comb(f(bt[0]), preOrderTraversal2(bt[1], comb, f, base), preOrderTraversal2(bt[2], comb, f, base))


'''
Practice for you at home... write a higher order in-order traversl and a higher-order post-order traversal

Extra Practice, rewrite preOrderTraversal2 so it does not take a base value, but instead takes a comb2 function.
  Find a process that differs in its result between the two versions! Can you write comb, comb2, and base across
  both calls to make them the same?
'''

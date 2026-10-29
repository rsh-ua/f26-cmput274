from cmput274 import *

def taxoPath(tree, cl):
  '''
  taxoPath returns a LList of all of the classifications of cl within the taxoTree tt

  tree    - TaxoTree
  cl      - a Str
  returns - LList of Str
  '''
  if tree == ():
    return empty()
  if tree[0] == cl:
    return LL(cl)
  children = tree[1]
  findThis = lambda t: taxoPath(t, cl)
  possiblePaths = map(findThis, children)
  # Map allowed us to apply taxoPath recursively to /every/ child of our
  # tree. We then know that at most one of them will have a path to the target!
  filteredPaths = filter(lambda p: not isEmpty(p), possiblePaths)
  # We can filter out the empty LLists from our results of taxoPath because
  # those were the subtrees that did not contain our target
  if isEmpty(filteredPaths):
    # if filteredPaths is empty /none/ of my children had a path to the
    # to the target... if I am not the target and NONE of my children have
    # a path to the target then I don't have a path to the target!
    return empty()
  return cons(tree[0], first(filteredPaths))
def main():
  taxoTree = (
    "Chordata",
    (
        (
            "Mammalia",
            (
                (
                   "Primates",
                    (
                        (
                            "Hominidae",
                            (
                                ("Homo sapiens", ()),
                                ("Pan troglodytes", ())
                            )
                        ),
                    )
                ),
                (
                    "Carnivora",
                    (
                        (
                            "Felidae",
                            (
                                ("Panthera leo", ()),
                                ("Panthera tigris", ())
                            )
                        ),
                    )
                )
            )
        ),
        (
            "Aves",
            (
                (
                    "Accipitriformes",
                    (
                        ("Cathartidae", ()),
                        ("Sagittariidae", ())
                    )
                ),
            )
        )
    ))
  testExact("t1", LL("Chordata", "Mammalia", "Primates"), taxoPath, taxoTree, "Primates")
  testExact("t2", LL("Chordata", "Aves", "Accipitriformes", "Cathartidae"), taxoPath, taxoTree, "Cathartidae")
  runTests()
if __name__ == "__main__":
  main()

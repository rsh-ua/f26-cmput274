from cmput274 import *

'''
A StmtTree is one of:
- LL("assign", ExprTree, ExprTree)
- LL("display", ExprTree)
- LL("repeat", ExprTree, LList of StmtTree)
- LL("mutate", ExprTree, ExprTree)
'''

def nextFreeMemoryLocation(mem):
  '''
  nextFreeMemoryLocation returns the next free memory location in a running fimpl program. The policy is simply to return 0
                         if the memory mapping is currently empty, otherwise return the next natural number that is the first unused
                         memory location (increment the largest one already in use).

  mem     - LList of LL(int, int), the current memory mapping of a fimpl program
  returns - int

  Examples:
    nextFreeMemoryLocation(empty()) -> 0
    nextFreeMemoryLocation(LL(LL(0, 5), LL(1, -23))) -> 2
  '''
  memLocs = map(lambda x: first(x), mem)
  largest = foldr(memLocs, lambda val, ror: val if val > ror else ror, -1)
  return largest+1


def replaceOrAdd(defns, key, val):
  pass

def tokensToStmtTree(tokens):
  '''
  tokensToStmtTree takes a LList of tokens and builds a StmtTree that represents the
                   first statement seen in tokens. It returns a LL(StmtTree, LList of str)
                   where the first item in the pair is the produced StmtTree and the 
                   second item in the pair is the remaining tokens.

  tokens  - LList of str, which represents tokens of a valid fimpl program
  returns - LL(StmtTree, LList of str)

  Side Effects: None

  Examples: 
    prog1 = "x <- 5\nDisp x\n x <- add x 1" 
    tokensToStmtTree(strToTokenList(prog1))
     -> (('assign', ('ident', 'x'), ('intLit', 5)), 
         ('Disp', 'x', 'x', '<-', 'add', 'x', '1'))
    
    prog2 = "Rpt x {\n y <- sub y 1\nDisp y\n}\nx <- add x 1"
    tokensToStmtTree(strToTokenList(prog2))
      -> (('repeat', 
            ('ident', 'x'), 
            (('assign', ('ident', 'y'), 
                        ('binOp', 'sub', 
                                  ('ident', 'y'), 
                                  ('intLit', 1))), 
              ('display', ('ident', 'y')))), 
          ('x', '<-', 'add', 'x', '1'))
      
  '''
  pass

def tokensToSTreeList(tokens):
  '''
  tokensToSTreeList takens a LList of tokens and returns a LList of StmtTree
                    that is the result of parsing all of the tokens into 
                    statements

  tokens  - LList of str, which represents tokens of a valid fimpl program
  returns - LList of StmtTree

  Side Effects: None

  Example:
    prog1 = "x <- 5\nDisp x\n x <- add x 1" 
    tokensToSTreeList(strToTokenList(prog1))
     -> (('assign', ('ident', 'x'), ('intLit', 5)), 
         ('display', ('ident', 'x')), 
         ('assign', ('ident', 'x'), ('binOp', 'add', ('ident', 'x'), ('intLit', 1))))
  '''
  pass
  

def runStmt(stmt, defns, mem, output):
  '''
  runStmt takes a single StmtTree and a LList of pairs that
          represent identifier definitions and executes the
          given statement, returning a 3-tuple of the updated
          definitions, memory, and output states.

  stmt    - a StmtTree, the statement to execute
  defns   - LList of LL(str, int), the identifier definitions
  mem     - LList of LL(int, int), the memory mapping
  output  - str
  returns - 3-tuple of (LList of LL(str, int), LList of LL(int, int), str)

  Examples:
    stmt0 = first(tokensToSTreeList(strToTokenList("x <- 3")))
    runStmt(stmt1, empty(), empty(), "") -> (LL(LL("x", 0)), LL(LL(0, 3)), "")

    stmt1 = first(tokensToSTreeList(strToTokenList("x <- add x 1")))
    runStmt(stmt1, LL(LL("x", 0)), LL(LL(0, 3)), "") -> (LL(LL("x", 1)), LL(LL(0, 3), LL(1, 4)), "")
  '''
  pass

def interp(text):
  '''
  interp is our fimpl interpreter. It takes a single string parameter that
         is a valid fimpl program and executes that program, returning the resultant state at the end of that programs execution.

  text    - str, a valid fimpl program
  returns - 3-tuple of (LList of LL(str, int), LList of LL(int, int), str)

  Examples:
    interp("x <- 1\nRpt 5 {\nDisp x\nx <- mul x 2\n}") -> (LL(LL("x", 5)), LL(LL(0, 1), LL(1, 2), LL(2, 4), LL(3, 8), LL(4, 16), LL(5, 32)), "1\n2\n4\n8\n16\n")
  '''
  pass


def testMain():
  testExact("replaceT1", LL(LL("y", 3), LL("x", 5)), replaceOrAdd, LL(LL("y", 3)), "x", 5)
  testExact("replaceT2", LL(LL("y", 17), LL("x", 5)), replaceOrAdd, LL(LL("y", 3), LL("x", 5)), "y", 17)
  testExact("replaceT3", LL(LL(0, 5), LL(1, -27)), replaceOrAdd, LL(LL(0, 5), LL(1, 77)), 1, -27)

  prog1 = "x <- 5\nDisp x\n x <- add x 1"
  result1 = LL(LL('assign', LL('ident', 'x'), LL('intLit', 5)), LL('Disp', 'x', 'x', '<-', 'add', 'x', '1')) 
  testExact("tokensToStmtTreeT1", result1, tokensToStmtTree, strToTokenList(prog1))

  prog2 = "Rpt x {\n y <- sub y 1\nDisp y\n}\nx <- add x 1"
  result2 = LL(LL('repeat', 
                  LL('ident', 'x'), 
                   LL(LL('assign', 
                        LL('ident', 'y'), 
                        LL('binOp', 'sub', 
                            LL('ident', 'y'), 
                            LL('intLit', 1))), 
                  LL('display', LL('ident', 'y')))), 
            LL('x', '<-', 'add', 'x', '1'))
  testExact("tokensToStmtTreeT2", result2, tokensToStmtTree, strToTokenList(prog2))


  prog3 = "x <- 5\nDisp x\n x <- add x 1" 
  result3 = LL(LL('assign', 
                  LL('ident', 'x'), 
                  LL('intLit', 5)), 
              LL('display', 
                  LL('ident', 'x')), 
              LL('assign', 
                  LL('ident', 'x'), 
                  LL('binOp', 'add', 
                    LL('ident', 'x'), 
                    LL('intLit', 1))))
  testExact("stmtListT1", result3, tokensToSTreeList, strToTokenList(prog3))

  stmt0 = first(tokensToSTreeList(strToTokenList("x <- 3")))
  testExact("runStmtT0", (LL(LL("x", 0)), LL(LL(0, 3)), ""), runStmt, stmt0, empty(), empty(), "")


  stmt1 = first(tokensToSTreeList(strToTokenList("x <- add x 1")))
  testExact("runStmtT1", (LL(LL("x", 1)), LL(LL(0, 3), LL(1, 4)), ""), runStmt, stmt1, LL(LL("x", 0)), LL(LL(0, 3)), "")

  stmt2 = first(tokensToSTreeList(strToTokenList("Disp sub x y")))
  testExact("runStmtT2", (LL(LL("x", 1486), LL("y", 2131)), LL(LL(1486, 2), LL(2131, 7)), "-5\n"), runStmt, stmt2, LL(LL("x", 1486), LL("y", 2131)), LL(LL(1486, 2), LL(2131, 7)), "")

  stmt3 = first(tokensToSTreeList(strToTokenList("Rpt 5 {\nx <- mul x 2\nDisp x\n}")))
  testExact("runStmtT3", (LL(LL("x", 5), LL("y", 0)),
                          LL(LL(0, 2), LL(1, 4), LL(2, 8), LL(3, 16), LL(4, 32), LL(5, 64)),
                          "5\n4\n8\n16\n32\n64\n"), runStmt, stmt3, LL(LL("x", 0), LL("y", 0)), LL(LL(0, 2)), "5\n")

  stmt4 = first(tokensToSTreeList(strToTokenList("Mutate x <- 9")))
  testExact("runStmtT4", (LL(LL("x", 0)),
                            LL(LL(0, 9)),
                            "5\n"), runStmt, stmt4, LL(LL("x", 0)), LL(LL(0, 2)), "5\n")

  fullProg1 = "x <- 1\nRpt 5 {\nDisp x\nx <- mul x 2\n}"
  testExact("interp1", (LL(LL("x", 5)), LL(LL(0, 1), LL(1, 2), LL(2, 4), LL(3, 8), LL(4, 16), LL(5, 32)), "1\n2\n4\n8\n16\n"), interp, fullProg1)

  fullProg2 = "x <- 1\ny <- x\nMutate x <- 7\nDisp y\n"
  testExact("interp2", (LL(LL("x", 0), LL("y", 0)), LL(LL(0, 7)), "7\n"), interp, fullProg2)

  runTests()


def main():
  '''
  Our main function is a bit different this time. When this program is executed it will ask for input from the
  user (you). You must enter either just the word tests if you would like to run the tests defined above (where you should
  also write your own tests), or you should enter the name of a plaintext file that contains a fimpl program that is
  stored in the same directory as your python program (or provide the path to a fimpl program if it resides elsewhere).

  This allows you to execute full fimpl programs easily by writing them in text files and providing them as the input when
  this program asks. It also will allow you to try the sample fimpl programs provided with the assignment once your
  interpreter is complete!
  '''
  choice = input("Enter the filename of the fimpl program you'd like to run or tests if you'd like to run the defined test cases: ")
  if choice != "tests":
    f = open(choice, "r")
    text = f.read()
    f.close()
    defns, mem, output = interp(text)
    print(output, end="")
  else:
    testMain()



if __name__ == "__main__":
  main()

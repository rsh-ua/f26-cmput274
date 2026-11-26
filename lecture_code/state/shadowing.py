id1 = "globalID1"
id2 = "globalID2"
def shadow():
  id1 = "shadowID1"
  def nestOne():
    id2 = "nestID2"
    return id1 + " - " + id2
  def nestTwo():
    return id1 + " - " + id2
  def nestThree(id1):
    return id1 + " - " + id2
  return (nestOne(), nestTwo(), nestThree("nestID1"))

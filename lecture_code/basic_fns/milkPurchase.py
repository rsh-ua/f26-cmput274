

def milkPurchase(alPrice, oatPrice, soyPrice):
  '''
  milkPurchase determines which type of milk, if any
               should be purchased out of almond, oat, or soy

  alPrice  - float, representing $cost/100ml of almond milk
  oatPrice - float, representing $cost/100ml of oat milk
  soyPrice - float, representing $cost/100ml of soy milk
  returns  - A string, one of "Almond", "Oat", "Soy", or "Nothing"

  Examples:
    milkPurchase(0.50, 0.25, 0.35) -> "Oat"
    milkPurcahse(0.35, 0.22, 0.19) -> "Soy"
    milkPurchase(0.6, 0.5, 0.45) -> "Nothing"
  '''
  almondLimit = 0.45
  oatLimit = 0.40
  soyLimit = 0.37
  globalLimit = 0.20
  if alPrice < globalLimit or (alPrice < almondLimit and oatPrice >= globalLimit and soyPrice >= globalLimit):
    return "Almond"
  # Note, as the above conditional returns that means that all the code following
  # has as a guarantee that it will not execute if this were a case where we were
  # to buy almond milk.
  # So in my future conditions I do not need to concern myself with the Almond milk price.
  if oatPrice < globalLimit or (oatPrice < oatLimit and soyPrice >= globalLimit):
    return "Oat"
  # Once again, after the above executes the function would be over if it were the
  # case that I would buy oat milk. As such, my future code can work under the assumption
  # that it is preconditioned with the fact that I will NOT buy oat milk in this scenario
  if soyPrice < soyLimit:
    return "Soy"
  # Now, my code can only reach this point if it were the case that I would not
  # purchase Almond, or Oat, or Soy milk in these conditions... so if I reach here
  # my answer is known:
  return "Nothing"

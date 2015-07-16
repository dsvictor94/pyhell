from pyhell import autoenable
from pyhell.hstypes import HaskellString, HaskellFunction
from Data.List import sort, take #import from haskell

two = HaskellFunction.from_string("2");
x = HaskellString(take(two, sort(HaskellString("pyhell"))))
#just checked the type and build the expression, it had not executed yet
print("the code", x.hs_code, "was not executed yet, simulating the lazily of Haskell: ", x._data)
print("now, when 'x' is direct accessed the code was evaluated and the result '", x, "' was cached to next use")
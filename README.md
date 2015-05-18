## pyhell

# require:

- "ghc" installed and available in the PATH
- "ghc-mod" installed and available in the PATH

# use:

```python
>>> from pyhell import autoenable
>>> from pyhell.hstypes import HaskellString
>>> from Data.List import sort #import from haskell
>>> x = HaskellString(sort(HaskellString("pyhell")))
>>> #just checked the type and build the expression, it had not executed yet
>>> print(x._data)
None
>>> print(x.hs_code)
(Data.List.sort "pyhell")
>>> print(x)
ehllpy
>>> #now the code was executed

# TODO

- rewrite the README
- write a decent setup.py
- check the function type and return the apropriete "hstype"
- write a lot of hstypes
- use ghc-mod as a server
- write a decent ghcmodwrapper


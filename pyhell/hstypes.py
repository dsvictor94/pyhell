import types
import inspect
import numbers
import collections

from pyhell.ghcwrapper import istype, execute

class HaskellFunction:

    wrappers = {}

    def __init__(self, func, module='Preload'):
        self.hs_code = "{}.{}".format(module, func)
        self.hs_type = None

    def __call__(self, *args):
        if len(args) == 0:
            return self
        code = "({})".format(self.hs_code)
        for arg in args:
            if type(arg) in self.__class__.wrappers:
                arg = HaskellFunction.wrappers[type(arg)]
            code = "({} {})".format(self.hs_code, arg.hs_code)
        return HaskellFunction.from_string(code)

    def __repr__(self):
        return "<haskell '{}'>".format(self.hs_code)

    @staticmethod
    def from_string(code, sig=''):
        f = HaskellFunction.__new__(HaskellFunction)
        f.hs_code = code
        f.hs_sig = sig
        return f


class HaskellString(collections.UserString, HaskellFunction):

    def __init__(self, data):
        if isinstance(data, HaskellFunction):
            if istype(data, "String"):
                self._data = None
                self.hs_code = data.hs_code
            else:
                raise ValueError(repr(data)+" is not a String")
        elif isinstance(data, str):
            self._data = data
            self.hs_code = '"{}"'.format(data)
        else:
            raise TypeError("HaskellString() argument must be a string or " 
                "a HaskellFunction, not '{}'".format(type(data).__name__))

    @property
    def data(self):
        if self._data is None:
            self._data = execute(self)[1:-2]
        return self._data

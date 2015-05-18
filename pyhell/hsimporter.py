from importlib import abc, util
from types import ModuleType
import sys
import keyword

from pyhell import ghcmodwrapper
from pyhell.hstypes import HaskellFunction


class HaskellFinder(abc.MetaPathFinder):

    _hs_modules = None

    @classmethod
    def _cached_hs_modules(cls):
        if not cls._hs_modules:
            cls._hs_modules = ghcmodwrapper.modules()
        return cls._hs_modules

    @classmethod
    def invalidate_caches(cls):
        cls._hs_modules = None

    @classmethod
    def find_spec(cls, fullname, path=None, target=None):
        modules = [m for m in path or cls._cached_hs_modules()
                        if m == fullname or m.startswith(fullname+'.')]
        if modules:
            spec = util.spec_from_loader(fullname, HaskellLoader,
                                         origin='haskell',
                                         is_package=len(modules) > 1)
            if len(modules) > 1:
                spec.submodule_search_locations = list(modules)
            return spec
        return None


class HaskellLoader(abc.Loader):

    def create_module(spec):
        mod = ModuleType(spec.name)
        return mod

    def exec_module(module):
        for func in ghcmodwrapper.browse(module.__name__):
            id = func.replace("'", "_")
            if keyword.iskeyword(id):
                id = "hs_"+id
            module.__dict__[id] = HaskellFunction(func, module.__name__)


def enable_import():
    sys.meta_path.append(HaskellFinder)
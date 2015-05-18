from setuptools import setup, find_packages
setup(
    name = "pyhell",
    version = "0.1",
    packages = find_packages(),
    install_requires = [],

    author = "Victor Duarte da Silva",
    description = "Import Haskell modules as normal python modules",
    license = "MIT",
    keywords = "python haskell import language binding FFI",
    url = "https://github.com/dsvictor94/pyhell",
)
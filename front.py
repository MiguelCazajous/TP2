"""
docstring
"""

import ctypes
import os

libPath="lib"
libName="libHelloWorld.so"


def loadLibrary():
    path=os.path.join(libPath, libName)
    libHelloWorld = ctypes.CDLL(path)
    #libHelloWorld.helloWorld.argtypes = (ctypes.c_int,)
    #libHelloWorld.factorial.restype = ctypes.c_ulonglong
    libHelloWorld.hello_world()


def main():
    """TODO: Docstring for main.
    :returns: TODO

    """
    loadLibrary()


if __name__ == "__main__":
    main()


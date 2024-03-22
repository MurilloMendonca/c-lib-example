# ctypes_test.py
import ctypes
import pathlib

if __name__ == "__main__":
    # Load the shared library into ctypes
    libname = pathlib.Path().absolute() / "libfoo.so"
    c_lib = ctypes.CDLL(libname)
    c_lib.print_hello()


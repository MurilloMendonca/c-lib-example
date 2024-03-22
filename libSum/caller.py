import ctypes
import pathlib

if __name__ == "__main__":
    libname = pathlib.Path().absolute() / "libsum.so"
    c_lib = ctypes.CDLL(libname)
    result = c_lib.sum(1, 2)
    print("1 + 2 = ", result)


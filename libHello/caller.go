package main

// #cgo LDFLAGS: -L. -l:libfoo.a
// #include "lib.h"
import "C"

func main() {
    C.print_hello()
}


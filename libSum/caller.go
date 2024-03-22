package main

// #cgo LDFLAGS: -L. -l:libsum.a
// #include "lib.h"
import "C"

import "fmt"

func main() {
    fmt.Printf("%d + %d = %d\n", 1,2,C.sum(1, 2))
}


all: lib-static lib-shared c-caller go-caller rust-caller wasm
clean:
	rm -f libsum.a lib.o libsum.so c-caller-static c-caller-shared go-caller-static go-caller-shared rust-caller-static rust-caller-shared libsum.wasm

lib-static: lib.c lib.h
	cc -c lib.c -o lib.o
	ar rcs libsum.a lib.o

lib-shared: lib.c lib.h
	cc -c lib.c -o lib.o
	cc -shared -o libsum.so lib.o

wasm:
	clang --target=wasm32 -nostdlib -Wl,--no-entry -Wl,--export-all -o libsum.wasm lib.c

c-caller: caller.c lib-static lib-shared
	cc caller.c -L. -l:libsum.a -o c-caller-static -static
	cc caller.c -L. -l:libsum.so -o c-caller-shared -Wl,-rpath=.

go-caller: caller.go lib-static lib-shared
	go build -o go-caller-static -ldflags="-linkmode external -extldflags -static" caller.go
	go build -o go-caller-shared caller.go

rust-caller: caller.rs lib-static lib-shared
	rustc caller.rs -L. -l static=lib:sum -C target-feature=+crt-static -o rust-caller-static
	rustc caller.rs -L. -l dylib=lib:sum -o rust-caller-shared -C link-arg=-Wl,-rpath,.


test: 
	./c-caller-static
	./c-caller-shared
	./go-caller-static
	./go-caller-shared
	./rust-caller-static
	./rust-caller-shared
	python3 caller.py
	node caller.js

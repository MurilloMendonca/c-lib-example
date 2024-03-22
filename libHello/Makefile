all: lib-static lib-shared c-caller go-caller rust-caller
clean:
	rm -f libfoo.a lib.o libfoo.so c-caller-static c-caller-shared go-caller-static go-caller-shared rust-caller-static rust-caller-shared

lib-static: lib.c lib.h
	cc -static -c lib.c -o lib.o
	ar rcs libfoo.a lib.o

lib-shared: lib.c lib.h
	cc -c lib.c -o lib.o
	cc -shared -o libfoo.so lib.o

wasm:
	clang --target=wasm32 -nostdlib -Wl,--no-entry -Wl,--export-all -o libfoo.wasm lib.c

c-caller: caller.c lib-static lib-shared
	$(CC) caller.c -L. -l:libfoo.a -o c-caller-static -static
	$(CC) caller.c -L. -l:libfoo.so -o c-caller-shared -Wl,-rpath=.

go-caller: caller.go lib-static lib-shared
	go build -o go-caller-static -ldflags="-linkmode external -extldflags -static" caller.go
	go build -o go-caller-shared caller.go

rust-caller: caller.rs lib-static lib-shared
	rustc caller.rs -L. -l static=lib:foo -C target-feature=+crt-static -o rust-caller-static
	rustc caller.rs -L. -l dylib=lib:foo -o rust-caller-shared -C link-arg=-Wl,-rpath,.


test: 
	./c-caller-static
	./c-caller-shared
	./go-caller-static
	./go-caller-shared
	./rust-caller-static
	./rust-caller-shared
	python3 caller.py

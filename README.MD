# C Library Example

This repository demonstrates how to create a C library and use it from multiple programming languages, including C, Go, Python, Rust, and JavaScript. It includes examples for two libraries: `libHello` and `libSum`, showcasing both static and shared library usage, as well as WebAssembly for use in web environments.


## Building and Running Examples

### Requirements

- GCC for compiling C code.
- Go compiler for Go examples.
- Rust compiler for Rust examples.
- Python3 for Python examples.
- Node.js for JavaScript examples.
- Emscripten SDK for compiling to WebAssembly (optional, only for JS examples).

### Instructions

To build and run the examples for a specific library, navigate to the library's directory and use the provided Makefile.

Example for `libSum`:

```sh
cd libSum
make all
make test
```

The Makefile includes targets for compiling static and shared versions of the libraries, as well as the callers in different languages:

- lib-static and lib-shared for compiling the library.
- c-caller, go-caller, rust-caller, and wasm for compiling the example programs.
- test for running all example programs.

### Cleaning up

To clean the build artifacts, use the clean target:

```sh
make clean
```

## Understanding the Makefile

Here's an overview of what each target in the Makefile does, using libSum/Makefile as an example:

- all: Builds everything required to run the examples.
- clean: Removes all compiled files.
- lib-static: Compiles a static library from the C source.
- lib-shared: Compiles a shared library from the C source.
- wasm: Compiles the library to WebAssembly using Clang.
- c-caller, go-caller, rust-caller: Compile the caller programs in C, Go, and Rust, linking them to the static or shared library as appropriate.
- test: Runs all compiled programs to demonstrate calling the library functions.

## Contributing

Contributions to improve the examples or add new ones are welcome. Please submit a pull request or open an issue to discuss your ideas.


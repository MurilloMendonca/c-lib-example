const fs = require('node:fs');

const wasmBuffer = fs.readFileSync('libsum.wasm');
WebAssembly.instantiate(wasmBuffer).then(wasmModule => {
    const { sum } = wasmModule.instance.exports;
    const result = sum(1, 2);
    console.log("1 + 2 = ", result);
});



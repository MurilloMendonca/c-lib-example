#[link(name = "lib", kind = "static")]
extern "C" {
    fn print_hello();
}

fn main() {
    unsafe {
        print_hello();
    }
}

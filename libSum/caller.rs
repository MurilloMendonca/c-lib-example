#[link(name = "lib", kind = "static")]
extern "C" {
    fn sum(a: i32, b: i32) -> i32;
}

fn main() {
    unsafe {
        let a = 1;
        let b = 2;
        let c = sum(a, b);
        println!("{} + {} = {}", a, b, c);
    }
}

fn panic_macro() {
    panic!("crash and burn");
}

fn do_some_panic() -> usize {
    let v = vec![1,2,3];
    v[99]
}

fn main() {
//    panic_macro();
    do_some_panic();
}
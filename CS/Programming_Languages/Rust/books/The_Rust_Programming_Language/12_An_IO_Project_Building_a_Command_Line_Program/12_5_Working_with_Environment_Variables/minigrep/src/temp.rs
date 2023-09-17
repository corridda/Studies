use std::env;

pub fn temp_func() {
    for (key, value) in env::vars() {
        println!("{key}: {value}");
    }
}

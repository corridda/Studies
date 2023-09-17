//! 18.2. Refutability: Whether a Pattern Might Fail to Match

fn refutable_pattern_is_not_accepted() {
    let some_option_value = Some(5);
//    let some_option_value: Option<i32> = None;
    if let Some(x) = some_option_value {
//    if let x = 5 {
        println!("x: {x}")
    }
    else {
        println!("x is None!");
    }
}

fn main() {
    refutable_pattern_is_not_accepted();
}

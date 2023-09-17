// **** Variables and Data Interacting with Move ****
fn vars_and_data_interacting_move() {
    let s1 = String::from("hello");
    let s2 = s1;

//    println!("{}, world!", s1);
    println!("{}, world!\n", s2);
}


// **** Variables and Data Interacting with Clone ****
fn vars_and_data_interacting_clone() {
    let s1 = String::from("hello");
    let s2 = s1.clone();

    println!("s1 = {s1}, s2 = {s2}\n");
}


// **** Stack-Only Data: Copy ****
fn stack_only_data_copy() {
    let x = 5;
    let y = x;

    println!("x = {}, y = {}", x, y);
}


fn main() {
    vars_and_data_interacting_move();
    vars_and_data_interacting_clone();
    stack_only_data_copy();
}

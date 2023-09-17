fn intro_option() {
    let some_number = Some(5);
    let some_char = Some('e');
    let absent_number: Option<i32> = None;

    println!("{0:?}\n{1:?}\n{2:?}", &some_number, &some_char, &absent_number);
}

fn main() {
    intro_option();
}

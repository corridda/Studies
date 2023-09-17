/// **** Removing Duplication by Extracting a Function ****
fn largest(list: &[i32]) -> Option<&i32> {
    match list.len() {
        0 => None,
        1 => Some(&list[0]),
        _ => {
            let mut largest_ = &list[0];
            for item in list {
                if item > largest_ {
                    largest_ = item;
                }
            }
            Some(largest_)
        }
    }
}

fn print_the_largest(v: Option<&i32>) {
    match v {
        Some(value) => println!("The largest value is: {0}\n", v.unwrap()),
        _ => println!("The list is empty!\n"),
    }
}

fn main() {
    let v = vec![15, 10, 8, 26, 3];
    print_the_largest(largest(&v));
    let v: Vec<i32> = Vec::new();
    print_the_largest(largest(&v));
    let arr = [1, 2, 5, 3];
    print_the_largest(largest(&arr));
}

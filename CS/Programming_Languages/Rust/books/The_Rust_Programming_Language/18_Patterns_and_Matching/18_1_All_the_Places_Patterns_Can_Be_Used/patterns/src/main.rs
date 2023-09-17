//! 18.1. All the Places Patterns Can Be Used

/// Conditional if let Expressions
fn if_let_expressions() {
    println!("if_let_expressions():");

    let favorite_color: Option<&str> = None;
    let is_tuesday = false;
    let age: Result<u8, _> = "34".parse();

    if let Some(color) = favorite_color {
        println!("Using your favorite color, {color}, as the background");
    } else if is_tuesday {
        println!("Tuesday is green day!");
    } else if let Ok(age) = age {
        if age > 30 {
            println!("Using purple as the background color");
        } else {
            println!("Using orange as the background color");
        }
    } else {
        println!("Using blue as the background color");
    }
    println!();
}

/// while let Conditional Loops
fn while_let() {
    println!("while_let():");

    let mut stack = Vec::new();
    stack.push(1);
    stack.push(2);
    stack.push(3);

    while let Some(top) = stack.pop() {
        println!("{top}");
    }
    println!();
}

/// for loops
fn for_loops() {
    println!("for_loops():");

    let v = vec!['a', 'b', 'c'];

    for (index, value) in v.iter().enumerate() {
        println!("{} is at index {}", value, index);
    }
    println!();
}

/// let Statements
fn let_statements() {
    println!("let_statements():");

    let (x, y, z) = (1, 2, 3);
    println!("x: {}, y: {}, z: {}", x, y, z);

    let (a, b, _, _) = (1, 2, 3, 4);
    println!("a: {}, b: {}", a, b);

    println!();
}

/// Function Parameters
fn function_params() {
    println!("function_params():");

    fn print_coordinates(&(x, y): &(i32, i32)) {
        println!("Current location: ({}, {})", x, y);
    }

    print_coordinates(&(5, 7));

    println!();
}

fn main() {
    if_let_expressions();
    while_let();
    for_loops();
    let_statements();
    function_params();
}

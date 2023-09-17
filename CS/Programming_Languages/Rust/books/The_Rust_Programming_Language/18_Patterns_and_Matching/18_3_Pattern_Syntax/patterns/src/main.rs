//! 18.3. Pattern Syntax

/// Matching Literals
fn matching_litarals() {
    println!("Inside matching_litarals()");

    let x = 5;

    match x {
        1 => println!("one\n"),
        2 => println!("two\n"),
        3 => println!("three\n"),
        _ => println!("something else\n"),
    }
}

/// Matching Named Variables
fn matching_named_variables() {
    println!("Inside matching_named_variables()");

    let x = Some(5);
    let y = 10;

    match x {
        Some(50) => println!("Got 50"),
        Some(y) => println!("Matched, y = {y}"),
        _ => println!("Default case, x = {:?}", x),
    }

    println!("at the end: x = {:?}, y = {y}\n", x);
}

/// Multiple Patterns
fn multiple_patterns() {
    println!("Inside multiple_patterns()");

    let x = 2;

    match x {
        1 | 2 => println!("one or two\n"),
        3 => println!("three\n"),
        _ => println!("anything\n"),
    }
}

/// Matching Ranges of Values with ..=
fn matching_ranges_of_values() {
    println!("Inside matching_ranges_of_values()");

    let x = 5;

    match x {
        1..=5 => println!("one through five"),
        _ => println!("something else"),
    }

    let x = 'c';

    match x {
        'a'..='j' => println!("early ASCII letter\n"),
        'k'..='z' => println!("late ASCII letter\n"),
        _ => println!("something else\n"),
    }
}

/// Destructuring to Break Apart Values
mod destructuring_to_break_apart_values {

    /// Destructuring Structs
    pub fn destructuring_structs() {
        println!("Inside destructuring_structs()");

        struct Point {
            x: i32,
            y: i32,
        }

        let p = Point { x: 0, y: 7 };
        let Point { x: a, y: b } = p;
        assert_eq!(0, a);
        assert_eq!(7, b);
        println!("Assertions were successful!");

        // Shorthand. The variables created in the let pattern are x and y instead of a and b.
        let Point { x, y } = p;
        println!("x: {x}, y: {y}");

        // Test some of the fields for particular values
        // while creating variables to destructure the other fields.
        match p {
            Point { x, y: 0 } => println!("On the x axis at {x}\n"),
            Point { x: 0, y } => println!("On the y axis at {y}\n"),
            Point { x, y } => println!("On neither axis: ({x}, {y})\n"),
        }
    }

    /// Destructuring Enums
    pub fn destructuring_enums() {
        println!("Inside destructuring_enums()");

        enum Message {
            Quit,
            Move { x: i32, y: i32 },
            Write(String),
            ChangeColor(i32, i32, i32),
        }

        let msg = Message::ChangeColor(0, 160, 255);
        //        let msg = Message::Move { x: 5, y: 10 };
        //        let msg = Message::Write("Some text to be displayed".to_string());

        match msg {
            Message::Quit => {
                println!("The Quit variant has no data to destructure.\n");
            }
            Message::Move { x, y } => {
                println!("Move in the x direction {x} and in the y direction {y}\n");
            }
            Message::Write(text) => {
                println!("Text message: {text}\n");
            }
            Message::ChangeColor(r, g, b) => {
                println!("Change the color to red {r}, green {g}, and blue {b}\n",)
            }
        }
    }

    /// Destructuring Nested Structs and Enums
    pub fn destructuring_nested_structs_and_enums() {
        println!("Inside destructuring_nested_structs_and_enums()");

        enum Color {
            Rgb(i32, i32, i32),
            Hsv(i32, i32, i32),
        }

        enum Message {
            Quit,
            Move { x: i32, y: i32 },
            Write(String),
            ChangeColor(Color),
        }

        let msg = Message::ChangeColor(Color::Hsv(0, 160, 255));

        match msg {
            Message::ChangeColor(Color::Rgb(r, g, b)) => {
                println!("Change color to red {r}, green {g}, and blue {b}\n");
            }
            Message::ChangeColor(Color::Hsv(h, s, v)) => {
                println!("Change color to hue {h}, saturation {s}, value {v}\n")
            }
            _ => (),
        }
    }

    /// Destructuring Structs and Tuples
    pub fn destructuring_structs_and_tuples() {
        println!("Inside destructuring_structs_and_tuples()");

        struct Point {
            x: i32,
            y: i32,
        }

        let ((feet, inches), Point { x, y }) = ((3, 10), Point { x: 15, y: 20 });
        println!("feet: {feet}\ninches: {inches}\nx: {x}, y: {y}\n")
    }
}

/// Ignoring Values in a Pattern
mod ignoring_values_in_a_pattern {

    /// Ignoring an Entire Value with _
    pub fn ignoring_an_entire_value_with_() {
        println!("Inside ignoring_an_entire_value_with_()");
                
        fn foo(_: i32, y: i32) {
            println!("This code only uses the y parameter: {}\n", y);
        }
        
        foo(3, 4);
    }

    /// Ignoring Parts of a Value with a Nested _
    pub fn ignoring_parts_of_a_value_with_a_nested_() {
        println!("Inside ignoring_parts_of_a_value_with_a_nested_()");
        
        let mut setting_value = Some(5);
//        let mut setting_value: Option<i32> = None;
        let new_setting_value = Some(10);

        match (setting_value, new_setting_value) {
            (Some(_), Some(_)) => {
                println!("Can't overwrite an existing customized value");
            }
            _ => {
                setting_value = new_setting_value;
            }
        }

        println!("setting is {:?}\n", setting_value);
        
        let numbers = (2, 4, 8, 16, 32);
        
        match numbers {
            (first, _, third, _, fifth) => {
                println!("Some numbers: {first}, {third}, {fifth}\n")
            },
        }
    }

    /// Ignoring an Unused Variable by Starting Its Name with _
    pub fn ignoring_unused_variable_by_starting_its_name_with_() {
        println!("Inside ignoring_unused_variable_by_starting_its_name_with_()");
        
        let _x = 5;
        let y = 10;
        
        let s = Some(String::from("Hello!"));

        if let Some(_) = s {
            println!("found a string");
        }

        println!("s: {:?}\n", s);
    }

    /// Ignoring Remaining Parts of a Value with ..
    pub fn ignoring_remaining_parts_of_value_with_ddot() {
        println!("Inside ignoring_remaining_parts_of_value_with_ddot()");
        
        struct Point {
            x: i32,
            y: i32,
            z: i32,
        }

        let origin = Point { x: 0, y: 0, z: 0 };
        
        match origin {
            Point { x, .. } => {
                println!("x: {x}")
            }
        }
        
        let numbers = (2, 4, 8, 16, 32);

        match numbers {
            (first, .., last) => {
                println!("Some numbers: {first}, {last}\n");
            }
        }
    }
}

/// Extra Conditionals with Match Guards
mod extra_conditionals_with_match_guards {
    
    pub fn extra_conditionals() {
        println!("Inside extra_conditionals()");
        
        let num = Some(4);
        
        match num {
            Some(x) if x % 2 == 0 => println!("The number {} is even", x),
            Some(x) => println!("The number {} is odd", x),
            None => (), 
        }
        
        let x = Some(5);
        let y = 10;

        match x {
            Some(50) => println!("Got 50"),
            Some(n) if n == y => println!("Matched, n = {n}"),
            _ => println!("Default case, x = {:?}", x),
        }

        println!("at the end: x = {:?}, y = {y}", x);
        
        let x = 4;
        let y = false;

        match x {
            4 | 5 | 6 if y => println!("yes\n"),
            _ => println!("no\n"),
        }
    }
}

/// @ Bindings
fn bindings() {
    println!("Inside bindings()");
    
    enum Message {
        Hello { id: i32 },
    }

    let msg = Message::Hello { id: 11 };

    match msg {
        Message::Hello {
            id: id_variable @ 3..=7,
        } => println!("Found an id in range: {}", id_variable),
        Message::Hello { id } if (10..=12).contains(&id) => {
            println!("Found an id in another range: {}", id)
        }
        Message::Hello { id } => println!("Found some other id: {}", id),
    }
}


fn main() {
    use destructuring_to_break_apart_values as destruct;
    use ignoring_values_in_a_pattern as ignoring;
    use extra_conditionals_with_match_guards as extra;

    matching_litarals();
    matching_named_variables();
    multiple_patterns();
    matching_ranges_of_values();
    
    destruct::destructuring_structs();
    destruct::destructuring_enums();
    destruct::destructuring_nested_structs_and_enums();
    destruct::destructuring_structs_and_tuples();
    
    ignoring::ignoring_an_entire_value_with_();
    ignoring::ignoring_parts_of_a_value_with_a_nested_();
    ignoring::ignoring_unused_variable_by_starting_its_name_with_();
    ignoring::ignoring_remaining_parts_of_value_with_ddot();
    
    extra::extra_conditionals();
    
    bindings();
}

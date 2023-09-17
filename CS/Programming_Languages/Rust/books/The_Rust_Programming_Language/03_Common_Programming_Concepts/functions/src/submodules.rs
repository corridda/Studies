// **** Parameters ****
pub mod parameters {
    pub fn another_function(x: i32) {
        println!("The value of x is: {x}");
    }

    pub fn print_labeled_measurement(value: i32, unit_label: char) {
        println!("The measurement is: {value}{unit_label}");
    }
}

//**** Statements and Expressions ****
pub mod statements_and_expressions {
    pub fn expression_example() {
        let y = {
            let x = 3;
            x + 1 // notice the absence of ';'
        };

        println!("The value of y is: {y}");
    }
}

// **** Functions with Return Values ****
pub mod functions_with_return_values {
    pub fn five() -> i32 {
        5
    }

    pub fn plus_one(x: i32) -> i32 {
        x + 1
    }
}

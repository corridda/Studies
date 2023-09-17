// **** Integer Types ****
pub mod integer_types {
    pub fn get_integer_types() {
        let x: i8 = 127;
        let y: u8 = 255;
        println!("x = {x}; type: {}", data_types::print_type_of(&x));
        println!("y = {y}; type: {}", data_types::print_type_of(&y));
        
        let x: i16 = 32767;
        let y: u16 = 65535;
        println!("x = {x}; type: {}", data_types::print_type_of(&x));
        println!("y = {y}; type: {}", data_types::print_type_of(&y));
        
        let x: i32 = 2147483647;
        let y: u32 = 4294967295;
        println!("x = {x}; type: {}", data_types::print_type_of(&x));
        println!("y = {y}; type: {}", data_types::print_type_of(&y));
        
        let x: i64 = 9223372036854775807;
        let y: u64 = 18446744073709551615;
        println!("x = {x}; type: {}", data_types::print_type_of(&x));
        println!("y = {y}; type: {}", data_types::print_type_of(&y));
        
        let x: i128 = 170141183460469231731687303715884105727;
        let y: u128 = 340282366920938463463374607431768211455;
        println!("x = {x}; type: {}", data_types::print_type_of(&x));
        println!("y = {y}; type: {}", data_types::print_type_of(&y));
        
        let hex_lit: u8 = 0xff;
        println!("hex_literal = {hex_lit}; type: {}", data_types::print_type_of(&hex_lit));
        
        let oct_lit: u8 = 0o77;
        println!("octal_literal = {oct_lit}; type: {}", data_types::print_type_of(&oct_lit));
        
        let bin_lit: u8 = 0b1111_0000;
        println!("binary_literal = {bin_lit}; type: {}", data_types::print_type_of(&bin_lit));
        
        let byte_lit: u8 = b'A';
        println!("byte_literal = {byte_lit}; type: {}\n", data_types::print_type_of(&byte_lit));
        
    }
}


// **** Floating-Point Types ****
pub mod float_types {
    pub fn get_float_types() {
        let x: f32 = 2.3;
        let y: f64 = 3.4;
        let z = 4.5;
        println!("x = {x}; type: {}", data_types::print_type_of(&x));
        println!("y = {y}; type: {}", data_types::print_type_of(&y));
        println!("z = {z}; type: {}\n", data_types::print_type_of(&z));
    }
}


// **** Numeric Operations ****
pub mod numeric_operations {
    pub fn do_some_math() {
        // addition
        let sum = 5 + 10;
        println!("5 + 10 = {sum}");

        // subtraction
        let difference = 95.5 - 4.3;
        println!("95.5 - 4.3 = {difference}");

        // multiplication
        let product = 4 * 30;
        println!("4 * 30 = {product}");

        // division
        let quotient = 56.7 / 32.2;
        println!("56.7 / 32.2 = {quotient}");
        let truncated = -5 / 3; // Results in -1
        println!("-5 / 3 = {truncated}");
                
        // remainder
        let remainder = 43 % 5;
        println!("43 % 5 = {remainder}\n");
    }
}


// **** The Character Type ****
pub mod character_type {
    pub fn get_char_type() {
        let c = 'z';
        let z: char = 'ℤ'; // with explicit type annotation
        let heart_eyed_cat = '😻';
        println!("c = {c}; type: {}", data_types::print_type_of(&c));
        println!("z = {z}; type: {}", data_types::print_type_of(&z));
        println!("z = {heart_eyed_cat}; type: {}\n", data_types::print_type_of(&heart_eyed_cat));
    }
}
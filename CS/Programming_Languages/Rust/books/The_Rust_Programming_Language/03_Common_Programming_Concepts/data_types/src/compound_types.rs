// **** The Tuple Type ****
pub mod tuple_type {
    pub fn get_tuple() {
        let tup: (i32, f64, u8) = (500, 6.4, 1);
        println!(
            "tup = {0:?}\ntype: {1}",
            tup,
            data_types::print_type_of(&tup)
        );
        let (_, y, _) = tup;
        println!("The value of y is: {y}");

        let x: (i32, f64, u8) = (500, 6.4, 1);
        let five_hundred = x.0;
        let six_point_four = x.1;
        let one = x.2;
        println!("five_hundred: {five_hundred}\nsix_point_four: {six_point_four}\none: {one}\n");
    }
}

// **** The Array Type ****
pub mod array_type {
    pub fn get_array() {
        let a: [i32; 5] = [1, 2, 3, 4, 5];
        println!("a: {a:?}");
        let months = ["January", "February", "March", "April", "May", "June", "July",
                      "August", "September", "October", "November", "December"];
        println!("months: {months:#?}");
        let b = [3; 5]; // [3, 3, 3, 3, 3]
        println!("b: {b:?}");
        
        // Accessing Array Elements
        let first = a[0];
        let second = a[1];
        println!("a: {a:?}\nfirst: {first}\nsecond: {second}\n")
    }
}

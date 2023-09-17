pub mod if_expressions {
    pub fn simple_if(number: i32) {
        if number < 5 {
            println!("less than 5");
        } else if number > 5 {
            println!("greater then 5");
        } else {
            println!("exactly 5");
        }
    }

    pub fn if_in_a_let(state: bool) -> &'static str {
        let res = if state {
            "state is true"
        } else {
            "state is false"
        };
        res
    }
}

pub mod loops {
    pub fn loop_loop() {
        let mut counter: u8 = 0;
        loop {
            if counter < 5 {
                println!("again!");
                counter += 1;
            } else {
                break;
            }
        }
    }

    pub fn loop_loop_with_counter() -> u8 {
        let mut counter: u8 = 0;
        loop {
            if counter < 5 {
                counter += 1;
            } else {
                break counter;
            }
        }
    }

    pub fn loop_lables() {
        let mut count = 0;
        'counting_up: loop {
            println!("count = {count}");
            let mut remaining = 10;

            loop {
                println!("remaining = {remaining}");
                if remaining == 9 {
                    break;
                }
                if count == 2 {
                    break 'counting_up;
                }
                remaining -= 1;
            }

            count += 1;
        }
        println!("End count = {count}");
    }

    pub fn loop_while() {
        let mut counter: u8 = 3;
        while counter != 0 {
            println!("{counter}!");
            counter -= 1;
        }
        println!("LIFTOFF!!!\n")
    }

    pub fn loop_for() {
        let a = [10, 20, 30];
        for element in a {
            println!("the value is: {element}")
        }
        println!()
    }

    pub fn loop_for_with_range() {
        // rev() is for reverting
        println!("Count from 3 to 1:");
        for n in (1..4).rev() {
            println!("{n}!")
        }
        println!("GO!\n")
    }
}

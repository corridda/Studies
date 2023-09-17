use std::net::IpAddr;

/// **** Cases in Which You Have More Information Than the Compiler ****
fn print_ip(ip: &String) {
    let ip_address: IpAddr = ip.parse().expect("Hardcoded IP address should be valid");
    println!("{ip_address}\n");
}

/// **** Creating Custom Types for Validation ****
pub struct Guess {
    value: i32,
}

impl Guess {
    pub fn new(value: i32) -> Guess {
        if value < 1 || value > 100 {
            panic!("Guess value must be between 1 and 100, got {}.", value);
        }

        Guess { value }
    }

    pub fn value(&self) -> i32 {
        self.value
    }
}


fn main() {
    let ip: String = String::from("127.0.0.1");
    print_ip(&ip);
    
    let guess_1 = Guess::new(55);
    println!("guess_1: {0}", guess_1.value);
    let guess_2 = Guess::new(101);  // panic!
}

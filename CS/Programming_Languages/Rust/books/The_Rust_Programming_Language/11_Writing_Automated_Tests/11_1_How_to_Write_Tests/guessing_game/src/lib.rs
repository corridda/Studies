// **** Checking for Panics with should_panic ****
pub struct Guess {
    value: u32,
}

impl Guess {
    pub fn new(value: u32) -> Guess {
        if value < 1 || value > 100 {
            if value < 1 {
                panic!(
                    "Guess value must be greater than or equal to 1, got {}.",
                    value
                );
            } else if value > 100 {
                panic!(
                    "Guess value must be less than or equal to 100, got {}.",
                    value
                );
            }
        }
        Guess { value }
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    // Checking for Panics with should_panic
    #[test]
    #[should_panic(expected = "be less than or equal to 100")]
    fn greater_than_100() {
        Guess::new(101);
    }

    // Using Result<T, E> in Tests
    #[test]
    fn it_works() -> Result<(), String> {
        if 2 + 2 == 4 {
            Ok(())
        } else {
            Err(String::from("two plus two does not equal four"))
        }
    }
}

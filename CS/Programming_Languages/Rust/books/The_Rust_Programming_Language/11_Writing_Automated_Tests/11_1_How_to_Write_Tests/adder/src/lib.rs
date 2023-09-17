// **** The Anatomy of a Test Function ****
pub fn add(left: usize, right: usize) -> usize {
    left + right
}

// **** Testing Equality with the assert_eq! and assert_ne! Macros ****
pub fn add_two(a: i32) -> i32 {
    a + 2
}

pub fn add_two_bugged(a: i32) -> i32 {
    a + 3
}

#[cfg(test)]
mod tests {
    use super::*;
    
    // **** The Anatomy of a Test Function ****
    #[test]
    fn exploration() {
        let result = add(2, 2);
        assert_eq!(result, 4);
    }

    #[test]
    fn another() {
        panic!("Make this test fail");
    }
    
    // **** Testing Equality with the assert_eq! and assert_ne! Macros ****
    #[test]
    fn it_adds_two() {
        assert_eq!(4, add_two(2));
        assert_eq!(4, add_two_bugged(2));
        assert_ne!(5, add_two(2));
    }

    #[test]
    fn it_adds_two_ne() {
        assert_ne!(5, add_two(2));
    }
}

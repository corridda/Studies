// **** Running a Subset of Tests by Name ****
pub fn add_two(a: i32) -> i32 {
    a + 2
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn add_two_and_two() {
        assert_eq!(4, add_two(2));
    }

    #[test]
    fn add_three_and_two() {
        assert_eq!(5, add_two(3));
    }

    #[test]
    fn one_hundred() {
        assert_eq!(102, add_two(100));
    }
}

#[cfg(test)]
mod tests2 {
    use super::*;

    #[test]
    fn add_four_and_two() {
        assert_eq!(6, add_two(4));
    }

    #[test]
    fn two_hundreds() {
        assert_eq!(202, add_two(200));
    }

    #[test]
    #[ignore]
    fn expensive_test() {
        for i in 0..10^3 {
            println!("{i}")
        }
    }
}

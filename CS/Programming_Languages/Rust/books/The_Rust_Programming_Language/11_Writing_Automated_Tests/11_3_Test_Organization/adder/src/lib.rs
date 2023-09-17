// **** Unit Tests ****
pub fn add_two(num: usize) -> usize {
    num + 2
}

fn internal_adder(a: usize, b: usize) -> usize {
    a + b
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_internal_adder() {
        let result = internal_adder(3, 4);
        assert_eq!(result, 7);
    }
}

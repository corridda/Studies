// **** Adding Custom Failure Messages ****
pub fn greeting(name: &str) -> String {
    format!("Hello {name}")
}

pub fn bugged_greeting(name: &str) -> String {
    String::from("Hello!")
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn greeting_contains_name() {
        let result = greeting("Carol");
        assert!(result.contains("Carol"));

        // Bugged greeting doesn't contain 'Carol'
        let result = bugged_greeting("Carol");
        assert!(
            result.contains("Carol"),
            "Greeting did not contain name, value was `{}`",
            result
        );
    }
}

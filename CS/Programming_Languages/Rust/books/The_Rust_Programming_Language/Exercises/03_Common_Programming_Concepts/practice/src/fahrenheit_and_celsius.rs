pub mod conversion {
    pub fn fahrenheit_to_celsius(far_degree: f64) -> f64 {
        (far_degree - 32.) / 1.8
    }
}
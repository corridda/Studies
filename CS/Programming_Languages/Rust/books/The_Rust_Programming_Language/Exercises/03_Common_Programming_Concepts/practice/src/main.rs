mod fahrenheit_and_celsius;
mod fibonacci;

use fahrenheit_and_celsius::conversion;
use fibonacci::fibo;

fn main() {
    println!("180.5 F = {} C", conversion::fahrenheit_to_celsius(180.5));
    
    // 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144.
    println!("Fibonacci(8)): {}", fibo::get_nth_fibo(8));
}

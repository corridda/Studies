struct Color(i32, i32, i32);
struct Point(i32, i32, i32);

fn main() {
    let black = Color(0, 0, 0);
    let origin = Point(0, 0, 0);
    
    println!("origin: ({0}, {1}, {2})", origin.0, origin.1, origin.2);
}

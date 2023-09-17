fn main() {
    let mut s = String::from("hello");
    println!("{s}");
    
    //push_str() appends a literal to a String
    s.push_str(", world!");
    
    println!("{s}");
}

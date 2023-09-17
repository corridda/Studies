fn first_word(s: &String) -> &str {
    let bytes = s.as_bytes();
    for (i, &item) in bytes.iter().enumerate() {
        if item == b' ' {
            return &s[..i];
        }
    }
    &s[..]
}


fn main() {
    let mut s = String::from("hello world");

//    let hello = &s[0..5];
    let hello = &s[..5];
//    let world = &s[6..11];
    let world = &s[6..];
    println!("{hello}\n{world}");
    
    let slice_1 = &s[0..s.len()];
    let slice_2 = &s[..];
    println!("{slice_1}\n{slice_2}\n");
    
    println!("The first word: {}", first_word(&s));
    
    // Let's clear 's' and try to get the first word again^
    s.clear();
    println!("The first word: {}\n", first_word(&s));
    
}

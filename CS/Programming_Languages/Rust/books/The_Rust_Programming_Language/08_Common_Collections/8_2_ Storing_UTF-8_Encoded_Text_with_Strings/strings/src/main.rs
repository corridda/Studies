// **** Creating a New String ****
fn create_string() {
    let mut s = String::new();
    
    let data = "initial contents";

    let s1 = data.to_string();

    // the method also works on a literal directly:
    let s2 = "initial contents".to_string();
    let s3 = String::from("initial contents");
    assert_eq!(s1, s2);
    let s4 = 10.to_string();
    println!("s1: {s1}\ns2: {s2}\ns3: {s3}\ns4: {s4}\n");
}


// **** Updating a String ****
fn update_string_push(s1: &mut String, s2: &String) {
    s1.push_str(s2);
}

fn update_string() {
    let mut s1 = String::from("foo");
    let s2 = "bar".to_string();
    update_string_push(&mut s1, &s2);
    
    let mut s3 = String::from("lo");
    s3.push('l');
    
    let s4 = String::from("Hello, ");
    let s5 = String::from("world!");
    let s6 = s4 + &s5; //note s4 has been moved here and can no longer be used
    
    let s7 = String::from("tic");
    let s8 = String::from("tac");
    let s9 = String::from("toe");
    let s10 = format!("{s7}-{s8}-{s9}");
    
    println!("s1: {s1}\ns2: {s2}\ns3: {s3}\ns6: {s6}\ns10: {s10}\n");
}


// **** Indexing into Strings ****
fn index_string() {
    let hello = String::from("Здравствуйте");
    println!("length: {0}", hello.len());
//    let answer = &hello[0];  // won't compile
    let answer = &hello[0..2];
    println!("answer: {answer}\n");
}


// **** Slicing Strings ****
fn slicing_string() {
    let hello = String::from("Здравствуйте");
    let s = &hello[0..4];
    println!("s: {s}\n");
}


// **** Methods for Iterating Over Strings ****
fn iterate_string(s: &String) {
    for c in s.chars() {
        println!("{c}");
    }
    println!();
    
    let mut bytes: Vec<u8> = Vec::new();
    for b in s.bytes() {
        bytes.push(b)
    }
    println!("bytes: {bytes:?}")
}


fn main() {
    create_string();
    update_string();
    index_string();
    slicing_string();
    iterate_string(&"Здр".to_string());
}

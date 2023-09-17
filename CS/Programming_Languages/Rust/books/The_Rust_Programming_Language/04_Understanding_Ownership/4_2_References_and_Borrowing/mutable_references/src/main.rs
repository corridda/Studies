fn main() {
    let mut s = String::from("Hello"); 
    change(&mut s);
    println!("{s}\n");
    
    // There migth be only one mutable reference to a mutable value
//    let r1 = &mut s;
//    let r2 = &mut s;
//    println!("{}, {}", r1, r2);
    
    // But one can use not simultaneous mutable references
    {
        let r1 = &mut s;
    }
    let r2 = &mut s;
    
    combine_mut_immut();
}

fn change(some_string: &mut String) {
    some_string.push_str(", world!");
}

fn combine_mut_immut() {
    let mut s = String::from("Hello");

    let r1 = &s; // no problem
    let r2 = &s; // no problem
    
    // There is no way to such a combining:
//    let r3 = &mut s; // BIG PROBLEM
//    println!("{}, {}, and {}", r1, r2, r3);
    
    // But if there won't be any exploitations of immutable references
    // forward on the code then you are able to make a mutable reference:
    println!("r1: {r1}\nr2: {r2}");
    let r_mut = &mut s;
    r_mut.push_str(", mutable world!");
    println!("r_mut: {r_mut}");
}

use lifetimes::*;

fn main() {
    out_of_scope();
    println!("The longest string is: {}", get_the_longest_string_slice());
    print_the_longest_string_slice();
    println!();
    
    // Lifetime Annotations in Struct Definitions
    let novel = String::from("Call me Ishmael. Some years ago...");
    let first_sentence = novel.split('.').next().expect("Could not find a '.'");
    let i = ImportantExcerpt {
        part: first_sentence,
    };
    println!("Lifetime Annotations in Struct Definitions");
    println!("i.part: {}\n", i.part);
    
    // Lifetime Annotations in Method Definitions
    println!("Lifetime Annotations in Method Definitions");
    println!("i.level(): {}", i.level());
    println!("i.announce_and_return_part(&str): {}\n", i.announce_and_return_part("Some announcment"));
    
    // The Static Lifetime
    println!("The Static Lifetime");
    let s: &'static str = "I have a static lifetime.";
    println!("s: {s}\n");
    
    // Generic Type Parameters, Trait Bounds, and Lifetimes Together
    println!("Generic Type Parameters, Trait Bounds, and Lifetimes Together");
    println!("{}\n", longest_with_an_announcement("short", "long string", "'anno'"));
}

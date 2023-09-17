use std::fmt::Display;

// **** Preventing Dangling References with Lifetimes ****
pub fn out_of_scope() {
    let mut r: Option<&i32> = None;
    {
        let x = 5;
        //        r = Some(&x); // no way to reference 'x' out of this scope
    }
    println!("r: {r:?}");
}

// **** Generic Lifetimes in Functions ****
// uncomment the following snippet
//fn longest(x: &str, y: &str) -> &str {
//    if x.len() > y.len() {
//        x
//    }
//    else {
//        y
//    }
//}

fn longest<'a>(x: &'a str, y: &'a str) -> &'a str {
    if x.len() > y.len() {
        x
    }
    else {
        y
    }
}

pub fn get_the_longest_string_slice<'a>() -> &'a str {
//    let s1 = String::from("abcd").as_str();
    let s1 = "abcd";
    let s2 = "xyz";
    longest(s1, s2)
}

// **** Lifetime Annotations in Function Signatures ****
pub fn print_the_longest_string_slice() {
    let string1 = String::from("long string is long");

    {
        let string2 = String::from("xyz");
        let result = longest(string1.as_str(), string2.as_str());
        println!("The longest string is '{}'", result);
    }
}

// **** Thinking in Terms of Lifetimes ****
fn first<'a>(x: &'a str, y: &str) -> &'a str {
    x
}

// **** Lifetime Annotations in Struct Definitions ****
pub struct ImportantExcerpt<'a> {
    pub part: &'a str
}

// **** Lifetime Elision ****
fn first_word(s: &str) -> &str {
    let bytes = s.as_bytes();

    for (i, &item) in bytes.iter().enumerate() {
        if item == b' ' {
            return &s[0..i];
        }
    }

    &s[..]
}

// **** Lifetime Annotations in Method Definitions ****
impl<'a> ImportantExcerpt<'a> {
    pub fn level(&self) -> i32 {
        3
    }
    
    pub fn announce_and_return_part(&self, announcement: &str) -> &str {
        println!("Attention please: {}", announcement);
        self.part
    }
}

// **** Generic Type Parameters, Trait Bounds, and Lifetimes Together ****
pub fn longest_with_an_announcement<'a, T>(
    x: &'a str,
    y: &'a str,
    ann: T,
    ) -> &'a str
where
    T: Display,
{
    println!("Announcement! {}", ann);
    if x.len() > y.len() {
        x
    } else {
        y
    }
}


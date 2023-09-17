// Convert strings to pig latin. The first consonant of each word is moved to the end
// of the word and “ay” is added, so “first” becomes “irst-fay.” Words that start with a vowel
// have “hay” added to the end instead (“apple” becomes “apple-hay”).
// Keep in mind the details about UTF-8 encoding!

fn pig_latin_string(s: &String) -> String {
    let vowels: Vec<char> = "aeiou".to_string().chars().collect();
//    println!("{0:?}", vowels);
    let str_chars_lower: Vec<char> = s.to_lowercase().chars().collect();
//    println!("{0}", str_chars_lower[0]);
    for vowel in vowels {
        if vowel == str_chars_lower[0] {
            return format!("{s}-hay");
        }
    }
    
    let str_chars: Vec<char> = s.chars().collect();
    let mut s_iter = s.chars();
    let first_consonent = s_iter.next().unwrap();
    format!("{0}-{first_consonent}ay", s_iter.as_str())
}

fn main() {
    let s1 = "apple".to_string();
    let pigged_s1 = pig_latin_string(&s1);
    println!("s1: {s1}\npigged_s1: {pigged_s1}");
    
    let s2 = "first".to_string();
    let pigged_s2 = pig_latin_string(&s2);
    println!("s2: {s2}\npigged_s2: {pigged_s2}")
}

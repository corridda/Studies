use std::collections::HashMap;

// **** Creating a New Hash Map ****
fn create_hash_map() -> HashMap<String, u32> {
    let mut scores = HashMap::new();
    scores.insert(String::from("Blue"), 10);
    scores.insert(String::from("Yellow"), 50);
    scores
}


// **** Accessing Values in a Hash Map ****
fn access_hash_map_values(hm: &HashMap<String, u32>, key: &String) -> u32 {
    hm.get(key).copied().unwrap_or(0)
}


// **** Hash Maps and Ownership ****
fn hash_map_ownership() {
    let field_name = String::from("Favorite color");
    let field_value = String::from("Blue");

    let mut map = HashMap::new();
    map.insert(field_name, field_value);
    println!("{map:#?}\n")
    
    // field_name and field_value are invalid at this point, try using them and
    // see what compiler error you get!
//    println!("{field_name}: {field_value}")
    
    // If we insert references to values into the hash map, the values won’t be moved into the hash map.
}


// **** Updating a Hash Map ****
// Overwriting a Value
fn overwrite_value(hm: &mut HashMap<String, u32>, key: String) {
    hm.insert(String::from(&key), 10);
    
    // The original value of 10 will overwritten.
    hm.insert(String::from(key), 25);
}

// Adding a Key and Value Only If a Key Isn’t Present
fn insert_50_if_key_not_present(hm: &mut HashMap<String, u32>, key: String) {
    hm.entry(key).or_insert(50);
}

// Updating a Value Based on the Old Value
fn count_words(text: String) {
    let mut map = HashMap::new();

    for word in text.split_whitespace() {
        let count = map.entry(word).or_insert(0);
        *count += 1;
    }

    println!("{:?}", map);
}



fn main() {
    let mut scores: HashMap<String, u32>  = create_hash_map();
    println!("{scores:#?}\n");
    
    // Access value
    let team_name = String::from("Blue");
    let score = access_hash_map_values(&scores, &team_name);
    println!("score: {score}\n");
    
    // Iterate through values
    println!("Iteration through the values:");
    for (key, value) in &scores {
        println!("{key}: {value}")
    }
    println!();
    
    hash_map_ownership();
    println!();
    
    // Overwrite value
    println!("Overwrite value:");
    overwrite_value(&mut scores, String::from("White"));
    println!("{scores:#?}\n");
    
    // Add value if it's not present
    println!("Add value if it's not present:");
    insert_50_if_key_not_present(&mut scores, "Blue".to_string());
    insert_50_if_key_not_present(&mut scores, "Red".to_string());
    println!("{scores:#?}\n");
    
    // Updating a Value Based on the Old Value
    count_words(String::from("hello world wonderful world"))
}

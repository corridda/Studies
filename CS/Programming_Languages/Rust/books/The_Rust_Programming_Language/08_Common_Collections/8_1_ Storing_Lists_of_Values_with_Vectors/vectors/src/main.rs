use vectors::get_type_of;

// **** Creating a New Vector ****
fn create_vector() {
    let v: Vec<i32> = Vec::new();
    println!("{v:?}");
    let v2 = vec![1, 2, 3];
    println!("{v2:?}");
    println!("{0}\n", get_type_of(&v2));
}


// **** Updating a Vector ****
fn update_vector() {
    let values: [i32; 3] = [4, 5, 6];
    let mut v: Vec<i32> = Vec::new();

    for val in values {
        v.push(val)
    }
    println!("{v:?}\n")
}


// **** Reading Elements of Vectors ****
fn reading_vectors_elements() {
    let v = vec![1, 2, 3, 4, 5];
    let third: &i32 = &v[2];
    println!("Third element: {third}");
    
    let forth: Option<&i32> = v.get(3);
    match forth {
        Some(forth) => println!("The forth element is {forth}\n"),
        None => println!("There is no forth element\n")
    }
}

fn mut_immut_refs() {
    let mut v = vec![1, 2, 3, 4, 5];
    
    // That won't compile since there you can’t have mutable and immutable references in the same scope.
    //    let first = &v[0];
    
    v.push(6);
    
    // But that's OK, cause you don't have mutable references after immutable ones.
    let first = &v[0];
    println!("The first element is: {first}\n");
}


// **** Iterating over the Values in a Vector ****
fn iterate_through_vector() {
    // Immutable references
    let v = vec![100, 32, 57];
    for i in &v {
        print!("{i} ");
    }
    println!();
    
    // Mutable references
    let mut v = vec![80, 70, 30];
    for i in &mut v {
        *i += 5;
    }
    println!("{v:?}\n")
    
}

// **** Using an Enum to Store Multiple Types ****
fn set_different_types() {
    #[derive(Debug)]
    enum SpreadsheetCell {
        Int(i32),
        Float(f64),
        Text(String),
    }

    let row = vec![
        SpreadsheetCell::Int(3),
        SpreadsheetCell::Text(String::from("blue")),
        SpreadsheetCell::Float(10.12),
    ];
    println!("{row:?}\n");
}


fn main() {
    create_vector();
    update_vector();
    reading_vectors_elements();
    mut_immut_refs();
    iterate_through_vector();
    set_different_types();
}

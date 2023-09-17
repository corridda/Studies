use std::fs::{self, File};
use std::io::{self, Read, ErrorKind};
use std::error::Error;

fn open_file(path: &String) {
    let file_result = File::open(path);
    println!("{0:?}\n", &file_result);
    let file_handler = match file_result {
        Ok(file) => file,
        Err(error) => panic!("Problem opening the file: {:?}", error),
    };
}

/// **** Matching on Different Errors ****
fn file_open_error_handling(path: &String) {
    let file_result = File::open(path);
    let file_handler = match file_result {
        Ok(file) => {
            println!("{0:?}\n", file.metadata());
            file
        }
        Err(error) => match error.kind() {
            ErrorKind::NotFound => match File::create(path) {
                Ok(fc) => {
                    println!("File '{path}' have been created.\n");
                    fc
                }
                Err(e) => panic!("Problem creating the file: {:?}", e),
            },
            other_error => {
                panic!("Problem opening the file: {:?}", other_error);
            }
        },
    };
}

/// **** Alternatives to Using match with Result<T, E> ****
fn file_open_error_handling_closures(path: &String) {
    let file_handler = File::open(path).unwrap_or_else(|error| {
        if error.kind() == ErrorKind::NotFound {
            File::create(path).unwrap_or_else(|error| {
                panic!("Problem creating the file: {:?}", error);
            })
        } else {
            panic!("Problem opening the file: {:?}", error);
        }
    });
    println!("{0:?}\n", file_handler.metadata());
}

/// **** Shortcuts for Panic on Error: unwrap and expect ****
fn get_ok_inside_or_panic_with_unwrap(path: &String) {
    let file_handler_result = std::fs::read_to_string(path);
    println!("{0}", file_handler_result.unwrap());
}

fn get_ok_inside_or_panic_with_expect(path: &String) {
    let file_handler_result = std::fs::read_to_string(path);
    println!("{0}", file_handler_result.expect("The certain file expected to be there..."));
}


/// **** Propagating Errors ****
fn read_username_from_file(path: &String) -> Result<String, io::Error> {
    let username_file_result = File::open(path);
    let mut username_file = match username_file_result {
        Ok(file) => file,
        Err(e) => return Err(e)
    };
    
    let mut username = String::new();
    match username_file.read_to_string(&mut username) {
        Ok(_) => Ok(username),
        Err(e) => Err(e)
    }
}


/// **** A Shortcut for Propagating Errors: the ? Operator ****
fn read_username_from_file_operator_ver1(path: &String) -> Result<String, io::Error> {
    let mut username_file_result = File::open(path)?;
    let mut username = String::new();
    username_file_result.read_to_string(&mut username)?;
    Ok(username)
}

fn read_username_from_file_operator_ver2(path: &String) -> Result<String, io::Error> {
    let mut username = String::new();
    File::open(path)?.read_to_string(&mut username)?;
    Ok(username)
}

fn read_username_from_file_operator_ver3(path: &String) -> Result<String, io::Error> {
    fs::read_to_string(path)
}


fn print_user_name(
    username_file_path: &String,
    func: fn(&String) -> Result<String, io::Error>) {
    
    let username_result = func(&username_file_path);
    let username = username_result.unwrap_or_else(|error| {
        if error.kind() == ErrorKind::NotFound {
            panic!("{error:?} It is expected that file with the user name is out there.");
        }
        else {
            panic!("{error:?} An unexpected error occured.");
        }
    });
    println!("User name is '{username}'\n");
}


/// **** Where The ? Operator Can Be Used ****
fn last_char_of_first_line(text: &str) -> Option<char> {
    text.lines().next()?.chars().last()
}


fn main() -> Result<(), Box<dyn Error>> {
    let file_path_1 = "c:\\hello.txt".to_string(); // Err
    let file_path_2 = "hello.txt".to_string(); // Ok
    let file_path_3 = "just_created_file.txt".to_string();
    //    open_file(&file_path_1);
    open_file(&file_path_2);

    println!("Error handling using matching:");
    file_open_error_handling(&file_path_2);
    file_open_error_handling(&file_path_3);

    println!("Using closure:");
    file_open_error_handling_closures(&file_path_2);

    println!("Using unwrap():");
    get_ok_inside_or_panic_with_unwrap(&file_path_2);
    //    get_ok_inside_or_panic_with_unwrap(&String::from(""));    // panic!
    
    println!("Using expect():");
    get_ok_inside_or_panic_with_expect(&file_path_2);
//        get_ok_inside_or_panic_with_expect(&String::from(""));    // panic!
    

    let username_file_path = "user_name.txt".to_string();

    println!("Read user name from a file:");
    print_user_name(&username_file_path, read_username_from_file);
    
    println!("Read user name from a file using ? operator [version 1]:");
    print_user_name(&username_file_path, read_username_from_file_operator_ver1);
   
    println!("Read user name from a file using ? operator [version 2]:");
    print_user_name(&username_file_path, read_username_from_file_operator_ver2);
    
    println!("Read user name from a file using ? operator [version 3]:");
    print_user_name(&username_file_path, read_username_from_file_operator_ver3);
    
    // Where The ? Operator Can Be Used
    let s = "aaa aaa\nbbb bbb".to_string();
    let empty_str = "".to_string();
    println!("{0:?}", last_char_of_first_line(&s));
    println!("{0:?}", last_char_of_first_line(&empty_str));
    
    let greeting_file = File::open("hello.txt")?;
    Ok(())
}

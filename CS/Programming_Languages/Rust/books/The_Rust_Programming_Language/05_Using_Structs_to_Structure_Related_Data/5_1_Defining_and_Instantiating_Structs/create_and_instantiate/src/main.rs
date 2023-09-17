struct User {
    active: bool,
    username: String,
    email: String,
    sign_in_count: u64,
}

fn build_user(email: String, username: String) -> User {
    User {
        active: true,
        username: username,
        email: email,
        sign_in_count: 1,
    }
}

// **** Using the Field Init Shorthand ****
fn build_user_field_init_shorthand(email: String, username: String) -> User {
    User {
        active: true,
        username,
        email,
        sign_in_count: 1,
    }
}



fn main() {
    let mut user1 = User {
        active: true,
        username: String::from("someusername123"),
        email: String::from("someone@example.com"),
        sign_in_count: 1,
    };
    println!("{}", user1.email);
    user1.email = String::from("anotheremail@example.com");
    println!("{}\n", user1.email);

    let new_user = build_user(
        String::from("new_user_email@gmail.com"),
        String::from("username_1"),
    );
    println!("{}\n", new_user.email);
    
    let new_user_2 = build_user(
        String::from("new_user_2_email@gmail.com"),
        String::from("username_2"),
    );
    println!("{}\n", new_user_2.email);   
}

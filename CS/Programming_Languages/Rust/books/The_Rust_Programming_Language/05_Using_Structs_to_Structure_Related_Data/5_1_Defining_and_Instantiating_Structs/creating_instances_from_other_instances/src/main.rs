struct User {
    active: bool,
    username: String,
    email: String,
    sign_in_count: u64,
}

fn main() {
    let user1 = User {
        active: true,
        username: String::from("someusername123"),
        email: String::from("someone@example.com"),
        sign_in_count: 1,
    };

    // Without the update syntax:
//    let user2 = User {
//        active: user1.active,
//        username: user1.username,
//        email: String::from("another@example.com"),
//        sign_in_count: user1.sign_in_count,
//    };
    
    // With the struct update syntax:
    let user2 = User {
        email: String::from("another@example.com"),
//        username: String::from("user_2_name"),
        // user1.username is moving to user2.username here and user1 is of no longer use 
        ..user1
    };
}

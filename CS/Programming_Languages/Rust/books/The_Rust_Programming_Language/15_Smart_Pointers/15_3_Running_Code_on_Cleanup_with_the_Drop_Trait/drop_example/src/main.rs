//! 15.3. Running Code on Cleanup with the Drop Trait

struct CustomSmartPointer {
    data: String,
}

impl Drop for CustomSmartPointer {
    fn drop(&mut self) {
        println!("Dropping CustomSmartPointer with data `{}`!", self.data);
    }
}

fn example_1() {
    let c = CustomSmartPointer {
        data: String::from("my stuff"),
    };
    let d = CustomSmartPointer {
        data: String::from("other stuff"),
    };
    println!("CustomSmartPointers created."); 
}

fn example_2() {
    let c = CustomSmartPointer {
        data: String::from("some data"),
    };
        println!("CustomSmartPointer created.");
        drop(c);
        println!("CustomSmartPointer dropped before the end of main.");
}

fn main() {
    println!("Example 1:");
    example_1();
    println!("\nExample 2:");
    example_2();
}

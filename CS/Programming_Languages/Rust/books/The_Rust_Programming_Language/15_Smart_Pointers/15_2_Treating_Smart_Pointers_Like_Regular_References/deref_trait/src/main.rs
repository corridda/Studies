//! # deref_trait crate
//! https://doc.rust-lang.org/book/ch15-02-deref.html

/// Following the Pointer to the Value
mod following_the_pointer_to_the_value {
    pub fn example() {
        let x = 5;
        let y = &x;

        assert_eq!(5, x);
        assert_eq!(5, *y);
    }
}

/// Using Box<T> Like a Reference
mod using_box_t_like_a_reference {
    pub fn example() {
        let x = 5;
        let y = Box::new(x);

        assert_eq!(5, x);
        assert_eq!(5, *y);
    }
}

/// Defining Our Own Smart Pointer
/// Treating a Type Like a Reference by Implementing the Deref Trait
mod defining_our_own_smart_pointer {
    use std::ops::Deref;

    pub struct MyBox<T>(T);

    impl<T> MyBox<T> {
        pub fn new(x: T) -> MyBox<T> {
            MyBox(x)
        }
    }

    impl<T> Deref for MyBox<T> {
        type Target = T;

        fn deref(&self) -> &Self::Target {
            &self.0
        }
    }

    pub fn example() {
        let x = 5;
        let y = MyBox::new(x);

        assert_eq!(5, x);
        assert_eq!(5, *y);
    }
}

/// Implicit Deref Coercions with Functions and Methods
mod implicit_deref_coercions_with_functions_and_methods {
    use crate::defining_our_own_smart_pointer::MyBox;
    
    fn hello(name: &str) {
        println!("Hello, {name}!");
    }

    pub fn example() {
        let m = MyBox::new(String::from("Rust"));
        hello(&m);
    }
}

fn main() {
    use defining_our_own_smart_pointer::example as ex3;
    use following_the_pointer_to_the_value::example as ex1;
    use using_box_t_like_a_reference::example as ex2;
    use implicit_deref_coercions_with_functions_and_methods::example as ex4;

    ex1();
    ex2();
    ex3();
    ex4();
}

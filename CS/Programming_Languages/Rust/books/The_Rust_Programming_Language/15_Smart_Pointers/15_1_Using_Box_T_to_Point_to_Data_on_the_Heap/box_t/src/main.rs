/// The Rust Programming Language
/// 15.1. Using Box<T> to Point to Data on the Heap
/// https://doc.rust-lang.org/book/ch15-01-box.html#enabling-recursive-types-with-boxes

mod box_t_to_store_data_on_the_heap {
    //! Using a Box<T> to Store Data on the Heap
    pub fn example() {
        let b = Box::new(5);
        println!("b = {b}");
    }
}

mod enabling_recursive_types_with_boxes {
    //! Enabling Recursive Types with Boxes
    #[derive(Debug)]
    enum List {
        Cons(i32, Box<List>),
        Nil,
    }
    
    pub fn example() {
        use List::{Cons, Nil};
        
        let list = Cons(1, Box::new(Cons(2, Box::new(Cons(3, Box::new(Nil))))));
        println!("{list:#?}")
    }
}

fn main() {
    use box_t_to_store_data_on_the_heap::example as ex1;
    use enabling_recursive_types_with_boxes::example as ex2;
    
    ex1();
    ex2();
}

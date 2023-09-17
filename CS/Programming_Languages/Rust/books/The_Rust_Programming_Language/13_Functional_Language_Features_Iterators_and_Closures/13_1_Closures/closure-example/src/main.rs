mod closure_type_inferense_and_annotation {
    /// Closure Type Inference and Annotation
    use std::thread;
    use std::time::Duration;

    pub fn run() {
        let expensive_closure = |num: u32| -> u32 {
            println!("calculating slowly...");
            thread::sleep(Duration::from_secs(2));
            num
        };
        println!("expensive_closure: {}", expensive_closure(5));

        fn add_one_v1(x: u32) -> u32 {
            x + 1
        }
        let add_one_v2 = |x: u32| -> u32 { x + 1 };
        let add_one_v3 = |x: u32| x + 1;
        let add_one_v4 = |x: u32| x + 1;

        let example_closure = |x| x;
        let param = example_closure(String::from("hello"));
        //    let param = example_closure(5);
        println!("param: {param}\n");
    }
}

mod capturing_references_or_moving_ownership {
    /// Capturing References or Moving Ownership
    use std::thread;

    pub fn run() {
        // A closure that captures an immutable reference
        let list = vec![1, 2, 3];
        println!(
            "The closure captures an immutable reference:\nBefore defining closure: {:?}",
            list
        );

        let only_borrows = || println!("From closure: {:?}", list);

        println!("Before calling closure: {:?}", list);
        only_borrows();
        println!("After calling closure: {:?}\n", list);

        // A closure that captures a mutable reference
        let mut list = vec![1, 2, 3];
        println!(
            "The closure captures a mutable reference:\nBefore defining closure: {:?}",
            list
        );

        let mut borrows_mutably = || list.push(7);

        borrows_mutably();
        println!("After calling closure: {:?}\n", list);

        // A closure that takes ownership
        let list = vec![1, 2, 3];
        println!(
            "The closure takes ownership:\nBefore defining closure: {:?}",
            list
        );

        thread::spawn(move || println!("From thread: {:?}", list))
            .join()
            .unwrap();
    }
}

mod moving_captured_values_out_of_closures {
    // Moving Captured Values Out of Closures and the Fn Traits
    #[derive(Debug)]
    struct Rectangle {
        width: usize,
        height: usize,
    }

    pub fn run() {
        let mut list = [
            Rectangle {
                width: 10,
                height: 1,
            },
            Rectangle {
                width: 3,
                height: 5,
            },
            Rectangle {
                width: 7,
                height: 12,
            },
        ];
        
        list.sort_by_key(|r| {
            r.width
        });
        
        println!("list:\n{list:?}\n");
        
        let mut list = [
            Rectangle { width: 10, height: 1 },
            Rectangle { width: 3, height: 5 },
            Rectangle { width: 7, height: 12 },
            ];

        let mut num_sort_operations = 0;
        let value = String::from("by key called");

        list.sort_by_key(|r| {
            num_sort_operations += 1;
            r.width
        });
        println!("{:?}, sorted in {num_sort_operations} operations\n", list);
    }
}

fn main() {
    //    closure_type_inferense_and_annotation::run();
    //    capturing_references_or_moving_ownership::run();
    moving_captured_values_out_of_closures::run();
}

//! 16.3. Shared-State Concurrency

use std::sync::{Arc, Mutex};
use std::thread;
use std::rc::Rc;

/// The API of Mutex<T>
fn api_mutex_t() {
    println!("Inside api_mutex_t():");
    let m = Mutex::new(5);
    {
        let mut num = m.lock().unwrap();
        *num = 6;
    }
    println!("m = {:?}\n", m);
}

/// Sharing a Mutex<T> Between Multiple Threads
/// Won't complile
//fn sharing_mutex_between_multiple_threads() {
//    println!("Inside sharing_mutex_between_multiple_threads():");
//    let counter = Mutex::new(0);
//    let mut handles = vec![];
//    
//    for _ in 0..10 {
//        let handle = thread::spawn(move || {
//            let mut num = counter.lock().unwrap();
//
//            *num += 1;
//        });
//        handles.push(handle);
//    }
//
//    for handle in handles {
//        handle.join().unwrap();
//    }
//
//    println!("Result: {}\n", *counter.lock().unwrap());
//}

/// Multiple Ownership with Multiple Threads
/// Won't complile either
//fn multiple_ownership() {
//    let counter = Rc::new(Mutex::new(0));
//    let mut handles = vec![];
//    
//    for _ in 0..10 {
//        let counter = Rc::clone(&counter);
//        let handle = thread::spawn(move || {
//            let mut num = counter.lock().unwrap();
//            *num += 1;
//        });
//        handles.push(handle);
//    }
//    
//    for handle in handles {
//        handle.join().unwrap();
//    }
//    
//    println!("Result: {}", *counter.lock().unwrap());
//}

/// Atomic Reference Counting with Arc<T>
fn atomic_reference_counting_with_arc_t() {
    let counter = Arc::new(Mutex::new(0));
    let mut handles = vec![];

    for _ in 0..10 {
        let counter = Arc::clone(&counter);
        let handle = thread::spawn(move || {
            let mut num = counter.lock().unwrap();

            *num += 1;
        });
        handles.push(handle);
    }

    for handle in handles {
        handle.join().unwrap();
    }

    println!("Result: {}", *counter.lock().unwrap());
}

fn main() {
    api_mutex_t();
//    sharing_mutex_between_multiple_threads();
//    multiple_ownership();
    atomic_reference_counting_with_arc_t();
}

//! 16.1. Using Threads to Run Code Simultaneously

use std::thread;
use std::time::Duration;

/// Creating a New Thread with spawn
fn spawn_thread() {
    println!("spawn_thread() is running:");
    thread::spawn(|| {
        for i in 1..10 {
            println!("hi number {} from the spawned thread!", i);
            thread::sleep(Duration::from_millis(1));
        }
    });

    for i in 1..5 {
        println!("hi number {} from the main thread!", i);
        thread::sleep(Duration::from_millis(1));
    }
    println!("");
}

/// Waiting for All Threads to Finish Using join Handles
fn use_join() {
    println!("use_join() is running:");
    let handle = thread::spawn(|| {
        for i in 1..10 {
            println!("hi number {} from the spawned thread!", i);
            thread::sleep(Duration::from_millis(1));
        }
    });

    for i in 1..5 {
        println!("hi number {} from the main thread!", i);
        thread::sleep(Duration::from_millis(1));
    }

    handle.join().unwrap();
    println!("");
}

/// Waiting for All Threads to Finish Using join Handles
/// Move handle.join() before the for loop
fn use_join_before_loop() {
    println!("use_join_before_loop() is running:");
    let handle = thread::spawn(|| {
        for i in 1..10 {
            println!("hi number {} from the spawned thread!", i);
            thread::sleep(Duration::from_millis(1));
        }
    });

    handle.join().unwrap();

    for i in 1..5 {
        println!("hi number {} from the main thread!", i);
        thread::sleep(Duration::from_millis(1));
    }
    println!("");
}

/// Using move Closures with Threads
pub mod using_move_closures_with_threads {
    use std::thread;

    pub fn using_move() {
        println!("using_move() is running:");
        let v = vec![1, 2, 3];
        let handle = thread::spawn(move || {
            println!("Here's a vector: {:?}", v);
        });

        handle.join().unwrap();
    }
}

fn main() {
    use using_move_closures_with_threads::using_move;

    spawn_thread();
    use_join();
    use_join_before_loop();
    using_move();
}

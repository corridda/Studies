//! 16.2. Using Message Passing to Transfer Data Between Threads
use std::sync::mpsc;
use std::thread;
use std::time::Duration;

fn create_channel_send_receive() {
    println!("create_channel_send_receive() is running:");
    let (tx, rx) = mpsc::channel();
    
    thread::spawn(move || {
        let val = String::from("hi");
        tx.send(val).unwrap();
    });
    
    let received = rx.recv().unwrap();
    println!("Got: {}", received);
    println!("");
}

/// Channels and Ownership Transference
fn ownership_transference() {
    println!("ownership_transference() is running:");
    let (tx, rx) = mpsc::channel();
    
    thread::spawn(move || {
        let val = String::from("hi");
        tx.send(val).unwrap();
        // uncomment to get the error[E0382]: borrow of moved value: `val`
//        println!("val is {}", val);
    });
    
    let received = rx.recv().unwrap();
    println!("Got: {}", received);
    println!("");
}

/// Sending Multiple Values and Seeing the Receiver Waiting
fn sending_multiple_values() {
    println!("sending_multiple_values() is running:");
    
    let (tx, rx) = mpsc::channel();

    thread::spawn(move || {
        let vals = vec![
            String::from("hi"),
            String::from("from"),
            String::from("the"),
            String::from("thread"),
        ];

        for val in vals {
            tx.send(val).unwrap();
            thread::sleep(Duration::from_secs(1));
        }
    });

    for received in rx {
        println!("Got: {}", received);
    }
    println!("");
}

/// Creating Multiple Producers by Cloning the Transmitter
fn multiple_producers() {
    println!("multiple_producers() is running:");
    
    let (tx, rx) = mpsc::channel();

    let tx1 = tx.clone();
    thread::spawn(move || {
        let vals = vec![
            String::from("hi"),
            String::from("from"),
            String::from("the"),
            String::from("thread"),
        ];

        for val in vals {
            tx1.send(val).unwrap();
            thread::sleep(Duration::from_secs(1));
        }
    });

    thread::spawn(move || {
        let vals = vec![
            String::from("more"),
            String::from("messages"),
            String::from("for"),
            String::from("you"),
        ];

        for val in vals {
            tx.send(val).unwrap();
            thread::sleep(Duration::from_secs(1));
        }
    });

    for received in rx {
        println!("Got: {}", received);
    }    
    println!("");
}

fn main() {
    create_channel_send_receive();
    ownership_transference();
    sending_multiple_values();
    multiple_producers();
}

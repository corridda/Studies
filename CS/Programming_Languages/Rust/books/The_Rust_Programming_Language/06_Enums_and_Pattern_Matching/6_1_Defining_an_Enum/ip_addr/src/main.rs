// **** Enum Values ****

#[derive(Debug)]
enum IpAddrKind {
    V4,
    V6,
}

#[derive(Debug)]
enum IpAddrEnum {
    V4(String),
    V6(String),
}

#[derive(Debug)]
enum IpAddrEnum_2 {
    V4(u8, u8, u8, u8),
    V6(String),
}

#[derive(Debug)]
struct IpAddr {
    kind: IpAddrKind,
    address: String,
}

#[derive(Debug)]
enum Message {
    Quit,
    Move { x: i32, y: i32 },
    Write(String),
    ChangeColor(i32, i32, i32),
}

impl Message {
    fn call(&self) {
        // method body would be defined here
        println!("Message::variant.call() was called...\n
The using type: {0}\n", ip_addr::print_type_of(&self));
    }
}


fn main() {
    let four = IpAddrKind::V4;
    let six = IpAddrKind::V6;

    let home = IpAddr {
        kind: IpAddrKind::V4,
        address: String::from("127.0.0.1"),
    };

    let loopback = IpAddr {
        kind: IpAddrKind::V6,
        address: String::from("::1"),
    };
    println!("home:\n{0:#?}\nloopback:\n{1:#?}\n", &home, &loopback);

    let home_2 = IpAddrEnum::V4(String::from("127.0.0.1"));
    let loopback_2 = IpAddrEnum::V6(String::from("::1"));
    println!(
        "home_2: {0:?}\nloopback_2: {1:?}\n",
        &home_2, &loopback_2
    );

    let home_3 = IpAddrEnum_2::V4(127, 0, 0, 1);
    let loopback_3 = IpAddrEnum_2::V6(String::from("::1"));
    println!(
        "home_3: {0:?}\nloopback_3: {1:?}\n",
        &home_3, &loopback_3
    );
    
    let m = Message::Write(String::from("hello"));
    m.call();
}

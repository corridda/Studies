fn match_control_flow() {
    let config_max = Some(3u8);
    println!("{config_max:?}");
    println!("{0}", config_max.unwrap());
    match config_max {
        Some(max) => println!("The maximum is configured to be {}\n", max),
        _ => (),
    }
}

// You can think of if let as syntax sugar for a match that runs code when the value
// matches one pattern and then ignores all other values.
fn if_let_control_flow() {
    let config_max = Some(5u8);
    if let Some(max) = config_max {
        println!("The maximum is configured to be {}\n", max);
    }
}

#[derive(Debug)]
enum UsState {
    Alabama,
    Alaska,
    // --snip--
}

enum Coin {
    Penny,
    Nickel,
    Dime,
    Quarter(UsState),
}

fn match_control_flow_2(coins: [Coin; 5]) {
    let mut count = 0;
    for coin in coins {
        match coin {
            Coin::Quarter(state) => println!("State quarter from {:?}!", state),
            _ => count += 1,
        }
    }
    println!("Non-qurter quantity: {count}\n");
}

fn run_match_control_flow_2() {
    match_control_flow_2([
        Coin::Penny,
        Coin::Nickel,
        Coin::Nickel,
        Coin::Penny,
        Coin::Quarter(UsState::Alaska),
    ]);
}

fn if_let_control_flow_2(coins: [Coin; 4]) {
    let mut count = 0;
    for coin in coins {
        if let Coin::Quarter(state) = coin {
            println!("State quarter from {:?}!", state)
        } else {
            count += 1;
        }
    }
    println!("Non-qurter quantity: {count}\n");
}

fn run_if_let_control_flow_2() {
    if_let_control_flow_2([
        Coin::Penny,
        Coin::Nickel,
        Coin::Nickel,
        Coin::Quarter(UsState::Alabama),
    ]);
}

fn main() {
    match_control_flow();
    if_let_control_flow();
    run_match_control_flow_2();
    run_if_let_control_flow_2();
}

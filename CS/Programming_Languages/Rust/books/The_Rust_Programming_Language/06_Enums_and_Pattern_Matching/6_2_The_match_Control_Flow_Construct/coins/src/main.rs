use rand::Rng;

// **** The match Control Flow Construct ****
enum Coin {
    Penny,
    Nickel,
    Dime,
    Quarter,
}

fn value_in_cents(coin: Coin) -> u8 {
    match coin {
        Coin::Penny => {
            println!("Lucky penny!");
            1
        }
        Coin::Nickel => 5,
        Coin::Dime => 10,
        //        Coin::Quarter => 25,
        _ => 25,
    }
}

fn run_value_in_cents() {
    println!("Coin nickel is of {0} cents", value_in_cents(Coin::Nickel));
    println!("Coin dime is of {0} cents", value_in_cents(Coin::Dime));
    println!(
        "Coin quarter is of {0} cents",
        value_in_cents(Coin::Quarter)
    );
    println!("Coin penny is of {0} cents\n", value_in_cents(Coin::Penny));
}

// **** Patterns That Bind to Values ****
#[derive(Debug)] // so we can inspect the state in a minute
enum UsState {
    Alabama,
    Alaska,
    // --snip--
}

enum Coin2 {
    Penny,
    Nickel,
    Dime,
    Quarter(UsState),
}

fn value_in_cents_2(coin: Coin2) -> u8 {
    match coin {
        Coin2::Penny => 1,
        Coin2::Nickel => 5,
        Coin2::Dime => 10,
        Coin2::Quarter(state) => {
            println!("State quarter from {:?}!", state);
            25
        }
    }
}

fn run_value_in_cents_2() {
    value_in_cents_2(Coin2::Quarter(UsState::Alaska));
    value_in_cents_2(Coin2::Quarter(UsState::Alabama));
    println!("");
}

// **** Matching with Option<T> ****
fn plus_one(x: Option<i32>) -> Option<i32> {
    match x {
        None => None,
        Some(i) => Some(i + 1),
    }
}

fn run_plus_one() {
    println!("9 + 1 = {0:?}", plus_one(Some(9)).unwrap());
    println!("Is it None? {0:?}", plus_one(None).is_none());
    println!("{0:?}\n", plus_one(None));
}

// **** Catch-all Patterns and the _ Placeholder ****
fn add_fancy_hat() {
    println!("Player got a fancy hat")
}

fn remove_fancy_hat() {
    println!("Player's hat was taken away")
}
fn move_player(num_spaces: u8) {
    println!("Player moved on {num_spaces} steps\n")
}

fn roll_dice(dice_roll: u8) {
    match dice_roll {
        3 => add_fancy_hat(),
        7 => remove_fancy_hat(),
        other => move_player(other),
    }
}

fn run_dice_roll() {
    roll_dice(3);
    roll_dice(7);
    roll_dice(9);
}

fn reroll() {
    println!("Rerolled...");
    let dice_roll = rand::thread_rng().gen_range(1..=12);
    roll_dice_2(dice_roll)
}

fn roll_dice_2(dice_roll: u8) {
    match dice_roll {
        3 => add_fancy_hat(),
        7 => remove_fancy_hat(),
        _ => reroll(),
    }
}

fn roll_dice_3(dice_roll: u8) {
    match dice_roll {
        3 => {
            println!();
            add_fancy_hat()
        }
        7 => remove_fancy_hat(),
        _ => (), // Nothing happens here...
    }
}

fn run_roll_dice_3() {
    roll_dice_3(3);
    roll_dice_3(7);
    roll_dice_3(8);
}

fn main() {
    run_value_in_cents();
    run_value_in_cents_2();
    run_plus_one();
    run_dice_roll();
    reroll();
    run_roll_dice_3();
}

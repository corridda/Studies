mod if_and_loop;

use if_and_loop::{
    if_expressions,
    loops,
};

fn main() {
    // if...else
    if_expressions::simple_if(6);
    println!("{}", if_expressions::if_in_a_let(true));
    println!("{}", if_expressions::if_in_a_let(false));
    
    // loops
    loops::loop_loop();
    println!("loop executed {} times\n", loops::loop_loop_with_counter());
    loops::loop_lables();
    println!();
    loops::loop_while();
    loops::loop_for();
    loops::loop_for_with_range();
}

mod submodules;

use submodules::{
    parameters,
    statements_and_expressions,
    functions_with_return_values,
};

fn main() {
    println!("Hello, world!");

    parameters::another_function(5);
    parameters::print_labeled_measurement(5, 'h');
    statements_and_expressions::expression_example();
    
    let res = functions_with_return_values::five();
    println!("Result of five(): {res}");
    
    let res = functions_with_return_values::plus_one(functions_with_return_values::five());
    println!("Result of plus_one(): {res}");
}

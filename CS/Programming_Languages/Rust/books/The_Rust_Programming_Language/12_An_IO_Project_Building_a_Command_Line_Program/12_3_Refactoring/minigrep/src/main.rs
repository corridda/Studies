use std::env;
use std::process;
use std::error::Error;

use minigrep::Config;

fn main() {
    let args: Vec<String> = env::args().collect();

    // Grouping Configuration Values
    //    let config = parse_config(&args);

    // Creating a Constructor for Config
    //    let config = Config::new(&args);

    // Returning a Result Instead of Calling panic!
    let config = Config::build(&args).unwrap_or_else(|err| {
        println!("Problem parsing arguments: {err}");
        process::exit(1);
    });
    
    // Handling Errors Returned from run in main
    if let Err(e) = minigrep::run(config) {
        println!("Application error: {e}");
        process::exit(1);
    }
}


//fn parse_config(args: &[String]) -> Config {
//    let query = args[1].clone();
//    let file_path = args[2].clone();
//    Config { query, file_path }
//}


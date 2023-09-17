use ::std::error::Error;
use std::fs;

pub struct Config {
    pub query: String,
    pub file_path: String,
}

//impl Config {
//    fn new(args: &[String]) -> Self {
//        // Improving the Error Message
//        if args.len() < 3 {
//            panic!("Not enough arguments!")
//        }
//
//        let query = args[1].clone();
//        let file_path = args[2].clone();
//        Config { query, file_path }
//    }
//}

// Returning a Result Instead of Calling panic!
impl Config {
    pub fn build(args: &[String]) -> Result<Self, &'static str> {
        if args.len() < 3 {
            return Err("Not enough arguments!");
        }
        let query = args[1].clone();
        let file_path = args[2].clone();
        Ok(Config { query, file_path })
    }
}

// Extracting Logic from main
pub fn run(config: Config) -> Result<(), Box<dyn Error>> {
    let contents = fs::read_to_string(config.file_path)?;

    println!("With text:\n{contents}");

    Ok(())
}

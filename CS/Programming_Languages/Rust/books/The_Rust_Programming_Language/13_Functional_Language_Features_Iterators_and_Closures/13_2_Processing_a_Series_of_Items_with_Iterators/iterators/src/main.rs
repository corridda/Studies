mod iter_intro {
    pub fn run() {
        // In Rust, iterators are lazy
        let v1 = vec![1, 2, 3];
        let v1_iter = v1.iter();

        for value in v1_iter {
            print!("{value} ");
        }
        println!();

        for value in v1.iter() {
            print!("{value} ");
        }
        println!();
    }
}

/// The Iterator Trait and the next Method
mod iter_trate_and_next_method {
    pub fn run() {
        
    }
}

fn main() {
    iter_intro::run();
}

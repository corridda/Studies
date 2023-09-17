//! 19.3. Advanced Types

/// Creating Type Synonyms with Type Aliases
mod creating_type_synonyms_with_type_aliases {
    use std::fmt;
    use std::io::Error;
    
    type Result<T> = std::result::Result<T, std::io::Error>;

    pub fn kilometers() {
        println!("Inside kilometers()");

        type Kilometers = i32;

        let x: i32 = 5;
        let y: Kilometers = 5;

        println!("x + y = {}\n", x + y);
    }

    pub fn manageable_lengthy_type() {
        println!("Inside manageable_lengthy_type()");

        type Thunk = Box<dyn Fn() + Send + 'static>;

        let f: Thunk = Box::new(|| println!("hi\n"));

        fn takes_long_type(f: Thunk) {
            f();
        }

        fn returns_long_type() -> Thunk {
            Box::new(|| println!("hi\n"))
        }

        takes_long_type(f);
    }

//    pub trait Write_wordy {
//        fn write(&mut self, buf: &[u8]) -> Result<usize, Error>;
//        fn flush(&mut self) -> Result<(), Error>;
//
//        fn write_all(&mut self, buf: &[u8]) -> Result<(), Error>;
//        fn write_fmt(&mut self, fmt: fmt::Arguments) -> Result<(), Error>;
//    }

    pub trait Write {
        fn write(&mut self, buf: &[u8]) -> Result<usize>;
        fn flush(&mut self) -> Result<()>;

        fn write_all(&mut self, buf: &[u8]) -> Result<()>;
        fn write_fmt(&mut self, fmt: fmt::Arguments) -> Result<()>;
    }
}

/// The Never Type that Never Returns
mod never_type_that_never_returns {
    
    fn never_ending() -> ! {
        println!("forever ");
        
        loop {
            print!("and ever... ")
        }
    }
    
}

fn main() {
    use creating_type_synonyms_with_type_aliases as type_syns;

    type_syns::kilometers();
    type_syns::manageable_lengthy_type();
}

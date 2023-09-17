//mod front_of_house {
//    pub mod hosting {
//        pub fn add_to_waitlist() {}
//    }
//}
//
//use crate::front_of_house::hosting;
//
//pub fn eat_at_restaurant() {
//    hosting::add_to_waitlist();
//}


//mod front_of_house {
//    pub mod hosting {
//        pub fn add_to_waitlist() {}
//    }
//}
//
//mod customer {
//    use crate::front_of_house::hosting;
//    
//    pub fn eat_at_restaurant() {
//        hosting::add_to_waitlist();
//    }
//}

//mod front_of_house {
//    pub mod hosting {
//        pub fn add_to_waitlist() {}
//    }
//}
//
//use crate::front_of_house::hosting;
//
//mod customer {
//
//    pub fn eat_at_restaurant() {
//        super::hosting::add_to_waitlist();
//    }
//}


// **** Creating Idiomatic use Paths ****
//use std::fmt;
//use std::io;
//
//fn function1() -> fmt::Result {
//    // --snip--
//}
//
//fn function2() -> io::Result<()> {
//    // --snip--
//}


// **** Providing New Names with the as Keyword ****
//use std::fmt::Result;
//use std::io::Result as IoResult;
//
//fn function1() -> Result {
//    // --snip--
//}
//
//fn function2() -> IoResult<()> {
//    // --snip--
//}


// **** Re-exporting Names with pub use ****
mod front_of_house {
    pub mod hosting {
        pub fn add_to_waitlist() {}
    }
}

pub use crate::front_of_house::hosting;

pub fn eat_at_restaurant() {
    hosting::add_to_waitlist();
}





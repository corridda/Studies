pub mod rectangles;

use rectangles::{
    using_vars,
    using_tuple,
    using_struct,
    using_struct_extended,
    using_struct_extended_2,
};

fn main() {
    using_vars();
    using_tuple();
    using_struct();
    using_struct_extended();
    using_struct_extended_2();
}

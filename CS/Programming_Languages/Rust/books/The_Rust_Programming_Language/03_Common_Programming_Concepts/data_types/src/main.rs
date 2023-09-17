mod scalar_types;
mod compound_types;

use scalar_types::{
    integer_types,
    float_types,
    numeric_operations,
    character_type,
};
use compound_types::{
    tuple_type,
    array_type,
};

fn main() {
    integer_types::get_integer_types();
    float_types::get_float_types();
    numeric_operations::do_some_math();
    character_type::get_char_type();
    tuple_type::get_tuple();
    array_type::get_array();
}

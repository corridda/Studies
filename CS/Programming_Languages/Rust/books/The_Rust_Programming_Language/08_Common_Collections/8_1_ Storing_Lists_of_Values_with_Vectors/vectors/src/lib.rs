
use std::any::type_name;

pub fn get_type_of<T>(_: &T) -> &str {
    // Get the given value type
    type_name::<T>()
}

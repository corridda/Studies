use std::any::type_name;

pub fn print_type_of<T>(_: &T) -> &str {
    type_name::<T>()
}
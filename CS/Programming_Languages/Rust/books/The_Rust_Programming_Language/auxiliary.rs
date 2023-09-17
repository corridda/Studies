use std::any::type_name;

pub fn get_type_of<T>(_: &T) -> &str {
    type_name::<T>()
}
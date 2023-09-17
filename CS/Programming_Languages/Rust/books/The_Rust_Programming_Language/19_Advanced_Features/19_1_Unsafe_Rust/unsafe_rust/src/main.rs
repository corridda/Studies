//! 19.1. Unsafe Rust

/// Dereferencing a Raw Pointer
mod dereferencing_raw_pointer {

    pub fn create_raw_pointers() {
        println!("Inside create_raw_pointers():");

        let mut num = 5;
        let r1 = &num as *const i32;
        let r2 = &mut num as *mut i32;

        //        // Usually, there is no good reason to write code like this, but it is possible.
        //        let address = 0x012345usize;
        //        let r = address as *const i32;

        // We use the dereference operator * on a raw pointer that requires an unsafe block
        unsafe {
            println!("r1 is {}", *r1);
            println!("r2 is {}\n", *r2);
        }
    }
}

/// Calling an Unsafe Function or Method
mod calling_unsafe_function_or_method {
    use std::vec;

    pub fn calling_unsafe_function() {
        println!("Inside calling_unsafe_function()");

        unsafe fn dangerous() {}

        unsafe {
            dangerous();
        }
        println!("");
    }

    /// Creating a Safe Abstraction over Unsafe Code
    pub fn create_unsafe_abstraction() {
        println!("Inside create_unsafe_abstraction()");

        let mut v = vec![1, 2, 3, 4, 5, 6];

        let r = &mut v[..];

        let (a, b) = r.split_at_mut(3);

        assert_eq!(a, &mut [1, 2, 3]);
        assert_eq!(b, &mut [4, 5, 6]);

        println!("");
    }

    fn split_at_mut(values: &mut [i32], mid: usize) -> (&mut [i32], &mut [i32]) {
        use std::slice;

        let len = values.len();
        let ptr = values.as_mut_ptr();

        assert!(mid <= len);

        unsafe {
            (
                slice::from_raw_parts_mut(ptr, mid),
                slice::from_raw_parts_mut(ptr.add(mid), len - mid),
            )
        }
    }

    pub fn call_split_at_mute() {
        println!("Inside call_split_at_mute()");

        let mut v = vec![1, 2, 3, 4, 5, 6];
        let ref_ = &mut v;

        let (a, b) = split_at_mut(ref_, 3);
        println!("a: {a:?}\nb: {b:?}\n");
    }

    /// Using extern Functions to Call External Code
    pub fn using_extern_functions() {
        println!("Inside using_extern_functions():");

        extern "C" {
            fn abs(input: i32) -> i32;
        }

        unsafe {
            println!("Absolute value of -3 according to C: {}\n", abs(-3));
        }
    }
}

/// Accessing or Modifying a Mutable Static Variable
mod accessing_or_modifying_mutable_static_variable {

    static HELLO_WORLD: &str = "Hello, world!";
    static mut COUNTER: u32 = 0;

    pub fn static_var_example() {
        println!("Inside static_var_example():");
        println!("{HELLO_WORLD}\n");
    }

    pub fn mutate_static_var() {
        println!("Inside mutate_static_var():");

        fn add_to_count(inc: u32) {
            unsafe {
                COUNTER += inc;
            }
        }

        add_to_count(3);

        unsafe {
            println!("COUNTER: {}", COUNTER);
        }
    }
}

fn main() {
    use accessing_or_modifying_mutable_static_variable as access_or_modify;
    use calling_unsafe_function_or_method as call_unsafe_func_method;
    use dereferencing_raw_pointer as deref_raw_pointer;

    deref_raw_pointer::create_raw_pointers();

    call_unsafe_func_method::calling_unsafe_function();
    call_unsafe_func_method::call_split_at_mute();
    call_unsafe_func_method::using_extern_functions();

    access_or_modify::static_var_example();
    access_or_modify::mutate_static_var();

}

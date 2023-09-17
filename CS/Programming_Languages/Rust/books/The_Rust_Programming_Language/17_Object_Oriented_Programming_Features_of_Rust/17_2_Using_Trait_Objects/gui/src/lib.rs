//! 17.2. Using Trait Objects That Allow for Values of Different Types

/// Defining a Trait for Common Behavior
pub trait Draw {
    fn draw(&self);
}

pub struct Screen {
    pub components: Vec<Box<dyn Draw>>,
}

impl Screen {
    pub fn run(&self) {
        for component in self.components.iter() {
            component.draw();
        }
    }
}

/// Implementing the Trait
pub struct Button {
    pub width: u32,
    pub height: u32,
    pub label: String,
}

impl Draw for Button {
    fn draw(&self) {
        println!("The Button instance was drawn.")
        
    }
}


pub mod alternative_screen_implementation {
//! An alternate implementation of the Screen struct and its run method using generics and trait bounds
    
    use super::Draw;
    pub struct Screen<T: Draw> {
        pub components: Vec<T>,
    }

    impl<T> Screen<T>
    where
        T: Draw,
    {
        pub fn run(&self) {
            for component in self.components.iter() {
                component.draw();
            }
        }
    }
}


#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn it_works() {
        
    }
}

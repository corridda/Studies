// Defining Methods
#[derive(Debug)]
struct Rectangle {
    width: u32,
    height: u32,
}

impl Rectangle {
    fn area(&self) -> u32 {
        self.width * self.height
    }

    fn width(&self) -> bool {
        self.width > 0
    }

    fn can_hold(&self, other: &Rectangle) -> bool {
        self.width > other.width && self.height > other.height
    }

    // assotiated function
    fn square(size: u32) -> Self {
        Self {
            width: size,
            height: size,
        }
    }
}

pub fn using_struct_with_method() {
    let rect1 = Rectangle {
        width: 30,
        height: 50,
    };

    println!(
        "The area of the rectangle is {} square pixels.",
        rect1.area()
    );

    if rect1.width() {
        println!("The rectangle has a nonzero width; it is {}", rect1.width);
    }
}

// Methods with More Parameters
pub fn using_struct_more_params() {
    let rect1 = Rectangle {
        width: 30,
        height: 50,
    };
    let rect2 = Rectangle {
        width: 10,
        height: 40,
    };
    let rect3 = Rectangle {
        width: 60,
        height: 45,
    };

    println!("Can rect1 hold rect2? {}", rect1.can_hold(&rect2));
    println!("Can rect1 hold rect3? {}", rect1.can_hold(&rect3));
}

// Associated Functions
pub fn associated_func_example() {
    let square_size = 10;
    let rect = Rectangle::square(square_size);
    println!("A square with the size of sides = 10:\n{rect:#?}");
}

// Multiple impl Blocks
pub fn multiple_impl_blocks() {
    struct Rectangle2 {
        width: u32,
        height: u32,
    }
    impl Rectangle2 {
        fn area(&self) -> u32 {
            self.width * self.height
        }
    }
    impl Rectangle2 {
        fn can_hold(&self, other: &Rectangle2) -> bool {
            self.width > other.width && self.height > other.height
        }
    }
    let rect1 = Rectangle2 {
        width: 30,
        height: 40
    };
    let rect2 = Rectangle2 {
        width: 15,
        height: 10
    };
    println!("Can rect1 hold rect2? {}", rect1.can_hold(&rect2));
}

// We’ll start by using single variables
pub fn using_vars() {
    let width1 = 30;
    let height1 = 50;

    println!(
        "The area of the rectangle is {} square pixels.",
        area(width1, height1)
    );
}

fn area(width: u32, height: u32) -> u32 {
    width * height
}

// Refactoring with Tuples
pub fn using_tuple() {
    let rect1: (u32, u32) = (30, 50);

    println!(
        "The area of the rectangle is {} square pixels.",
        area_using_tuple(rect1)
    );
}

fn area_using_tuple(dimensions: (u32, u32)) -> u32 {
    dimensions.0 * dimensions.1
}

// Refactoring with Structs: Adding More Meaning
#[derive(Debug)]
struct Rectangle {
    width: u32,
    height: u32,
}

pub fn using_struct() {
    let rectangle = Rectangle {
        width: 30,
        height: 50
    };

    println!(
        "The area of the rectangle is {} square pixels.",
        area_using_struct(&rectangle)
    );
}

fn area_using_struct(rectangle: &Rectangle) -> u32 {
    rectangle.width * rectangle.height
}

// Adding Useful Functionality with Derived Traits
pub fn using_struct_extended() {
    let rectangle = Rectangle {
        width: 30,
        height: 50
    };

    println!("rectangle: {rectangle:?}");
    println!("rectangle: {rectangle:#?}");
}

// dbg! macro
pub fn using_struct_extended_2() {
    let scale = 2;
    let rectangle = Rectangle {
        width: dbg!(scale * 30),
        height: 50
    };

    // Here rectangled will be moved
//    dbg!(rectangle);
    
    // But we don't wand it to be moved, so let's borrow it instead:
    dbg!(&rectangle);
    println!("rectangle: {rectangle:#?}");
}
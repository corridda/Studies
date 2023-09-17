// **** In Function Definitions ****

fn largest_i32(list: &[i32]) -> &i32 {
    let mut largest = &list[0];

    for item in list {
        if item > largest {
            largest = item;
        }
    }

    largest
}

fn largest_char(list: &[char]) -> &char {
    let mut largest = &list[0];

    for item in list {
        if item > largest {
            largest = item;
        }
    }

    largest
}

fn largest<T: std::cmp::PartialOrd>(list: &[T]) -> &T {
    let mut largest = &list[0];

    for item in list {
        if item > largest {
            largest = item;
        }
    }

    largest
}


// **** In Struct Definitions ****
#[derive(Debug)]
struct Point<T> {
    x: T,
    y: T,
}

#[derive(Debug)]
struct PointMult<T, U> {
    x: T,
    y: U,
}


// **** In Method Definitions ****
#[derive(Debug)]
struct PointWithMethod<T> {
    x: T,
    y: T,
}

impl<T> PointWithMethod<T> {
    fn x(&self) -> &T {
        &self.x
    }
}

impl PointWithMethod<f32> {
    fn distance_from_origin(&self) -> f32 {
        (self.x.powi(2) + self.y.powi(2)).sqrt()
    }
}

struct PointXY<X1, Y1> {
    x: X1,
    y: Y1,
}

impl<X1, Y1> PointXY<X1, Y1> {
    fn mixup<X2, Y2>(self, other: PointXY<X2, Y2>) -> PointXY<X1, Y2> {
        PointXY {
            x: self.x,
            y: other.y,
        }
    }
}




fn main() {
    // In Function Definitions
    let number_list = vec![34, 50, 25, 100, 65];

    let result = largest_i32(&number_list);
    println!("The largest number is {}", result);

    let char_list = vec!['y', 'm', 'a', 'q'];

    let result = largest_char(&char_list);
    println!("The largest char is {}\n", result);
    
    println!("largest() function:");
    println!("The largest number is {}", largest(&number_list));
    println!("The largest char is {}\n", largest(&char_list));
    
    
    // In Struct Definitions
    let integer = Point {x: 5, y: 10};
    let float = Point { x: 1.0, y: 4.0 };
    println!("integer point: {integer:?}\nfloat point: {float:?}");
    
//    let wont_work = Point { x: 5, y: 4.0 };
    // Multiple generic type parameters.
    let integer_and_float = PointMult { x: 5, y: 4.0 };
    println!("integer_and_float: {integer_and_float:?}");
    
    
    // In Method Definitions
    let p = PointWithMethod {x: 5, y: 10};
    println!("p.x: {0}", p.x());
    
    let p = PointWithMethod {x: 5., y: 10.};
    println!("sqrt(p.x^2 + p.y^2): {0}\n", p.distance_from_origin());
    
    let p1 = PointXY { x: 5, y: 10.4 };
    let p2 = PointXY { x: "Hello", y: 'c' };
    let p3 = p1.mixup(p2);
    println!("p3.x = {}, p3.y = {}", p3.x, p3.y);
    
}

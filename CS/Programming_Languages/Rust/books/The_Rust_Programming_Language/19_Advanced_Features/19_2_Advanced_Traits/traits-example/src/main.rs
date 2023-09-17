//! 19.2. Advanced Traits

/// Specifying Placeholder Types in Trait Definitions with Associated Types
mod specifying_placeholder_types_in_trait_definitions {

    pub trait MyTrait {
        type Item;

        fn my_func(&self) -> Option<Self::Item>;
    }

    struct MyItem {
        item: i32,
    }

    impl MyTrait for MyItem {
        type Item = i32;

        fn my_func(&self) -> Option<Self::Item> {
            match self.item {
                0..=100 => Some(self.item),
                _ => None,
            }
        }
    }

    pub fn associated_type() {
        println!("Inside associated_type()");

        let new_item = MyItem { item: 10 };
        println!("new_item.item: {:?}\n", new_item.my_func());
    }
}

/// Default Generic Type Parameters and Operator Overloading
mod default_generic_type_parameters_and_operator_overloading {

    use std::ops::Add;

    #[derive(Debug, Copy, Clone, PartialEq)]
    struct Point {
        x: i32,
        y: i32,
    }

    impl Add for Point {
        // <PlaceholderType=ConcreteType>
        type Output = Point;

        fn add(self, other: Point) -> Point {
            Point {
                x: self.x + other.x,
                y: self.y + other.y,
            }
        }
    }

    pub fn make_assirtion_point() {
        assert_eq!(
            Point { x: 1, y: 1 } + Point { x: 2, y: 2 },
            Point { x: 3, y: 3 }
        );
    }

    #[derive(Debug, Copy, Clone, PartialEq)]
    struct Millimeters(u32);
    struct Meters(u32);

    impl Add for Millimeters {
        type Output = Millimeters;

        fn add(self, rhs: Self::Output) -> Self::Output {
            Millimeters(self.0 + rhs.0)
        }
    }

    impl Add<Meters> for Millimeters {
        type Output = Millimeters;

        fn add(self, rhs: Meters) -> Self::Output {
            Millimeters(self.0 + (rhs.0 * 1000))
        }
    }

    pub fn make_asserion_millimeters() {
        assert_eq!(Millimeters(1500), Millimeters(500) + Meters(1));
        assert_eq!(Millimeters(1500), Millimeters(300) + Millimeters(1200))
    }
}

/// Fully Qualified Syntax for Disambiguation: Calling Methods with the Same Name
mod fully_qualified_syntax_for_disambiguation {

    trait Pilot {
        fn fly(&self);
    }

    trait Wizard {
        fn fly(&self);
    }

    struct Human;

    impl Pilot for Human {
        fn fly(&self) {
            println!("This is your captain speaking.");
        }
    }

    impl Wizard for Human {
        fn fly(&self) {
            println!("Up!");
        }
    }

    impl Human {
        fn fly(&self) {
            println!("*waving arms furiously*");
        }
    }

    pub fn get_human_flying() {
        println!("Inside get_human_flying()");

        let person = Human;
        person.fly();
        Pilot::fly(&person);
        Wizard::fly(&person);
        println!();
    }

    // associated functions
    trait Animal {
        fn baby_name() -> String;
    }

    struct Dog;

    impl Dog {
        fn baby_name() -> String {
            String::from("Spot")
        }
    }

    impl Animal for Dog {
        fn baby_name() -> String {
            String::from("puppy")
        }
    }

    pub fn name_dog_as_dog_and_as_animal() {
        println!("Inside name_dog_as_dog_and_as_animal()");

        println!("A baby dog is called a {}", Dog::baby_name());
        println!("A baby dog is called a {}\n", <Dog as Animal>::baby_name());
    }
}

/// Using Supertraits to Require One Trait’s Functionality Within Another Trait
mod using_supertraits {

    use std::fmt;

    trait OutlinePrint: fmt::Display {
        fn outline_print(&self) {
            let output = self.to_string();
            let len = output.len();
            println!("{}", "*".repeat(len + 4));
            println!("*{}*", " ".repeat(len + 2));
            println!("* {} *", output);
            println!("*{}*", " ".repeat(len + 2));
            println!("{}\n", "*".repeat(len + 4));
        }
    }

    struct Point {
        x: i32,
        y: i32,
    }

    impl fmt::Display for Point {
        fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
            write!(f, "({}, {})", self.x, self.y)
        }
    }

    impl OutlinePrint for Point {}

    pub fn print_point() {
        println!("Inside print_point()");
        
        let point = Point {
            x: 5,
            y: 7,
        };
        
        point.outline_print();
    }
}

/// Using the Newtype Pattern to Implement External Traits on External Types
mod using_newtype_pattern {
    
    use std::fmt;
    
    struct Wrapper(Vec<String>);
    
    impl fmt::Display for Wrapper {
        fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
            write!(f, "[{}]", self.0.join(", "))
        }
    }

    pub fn print_vec_string() {
        println!("Inside print_vec_string()");
        let w = Wrapper(vec![String::from("Hello"), String::from("world")]);
        println!("{w}\n");
    }
    
}

fn main() {
    use default_generic_type_parameters_and_operator_overloading as def_gen_type_params;
    use fully_qualified_syntax_for_disambiguation as fq_syntax;
    use specifying_placeholder_types_in_trait_definitions as spec_plhr;
    use using_supertraits;
    use using_newtype_pattern;

    spec_plhr::associated_type();
    def_gen_type_params::make_assirtion_point();
    def_gen_type_params::make_asserion_millimeters();
    fq_syntax::get_human_flying();
    fq_syntax::name_dog_as_dog_and_as_animal();
    using_supertraits::print_point();
    using_newtype_pattern::print_vec_string();
}

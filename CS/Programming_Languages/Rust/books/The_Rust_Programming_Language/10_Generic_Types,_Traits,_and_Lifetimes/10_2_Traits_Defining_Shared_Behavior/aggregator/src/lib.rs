use std::fmt::{self, Display};

// **** Defining a Trait ****
pub trait Summary {
    fn summarize(&self) -> String;
}

// **** Implementing a Trait on a Type ****
pub struct NewsArticle {
    pub headline: String,
    pub location: String,
    pub author: String,
    pub content: String,
}

impl Summary for NewsArticle {
    fn summarize(&self) -> String {
        format!("{}, by {} ({})", self.headline, self.author, self.location)
    }
}

impl SummaryDefaultImpl for NewsArticle {}

impl Display for NewsArticle {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        write!(f, "({}, {})", self.headline, self.author)
    }
}

pub struct Tweet {
    pub username: String,
    pub content: String,
    pub reply: bool,
    pub retweet: bool,
}

impl Summary for Tweet {
    fn summarize(&self) -> String {
        format!("{}: {}", self.username, self.content)
    }
}

impl SummaryDefaultImpl for Tweet {}

impl SummaryDefaultImpl_2 for Tweet {
    fn summarize_author(&self) -> String {
        format!("@{}", self.username)
    }
}

impl Display for Tweet {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        write!(f, "({}, {})", self.username, self.content)
    }
}

// **** Default Implementations ****
pub trait SummaryDefaultImpl {
    fn summarize(&self) -> String {
        String::from("(Read more...)")
    }
}

pub trait SummaryDefaultImpl_2 {
    fn summarize_author(&self) -> String;

    fn summarize(&self) -> String {
        format!("(Read more from {}...)", self.summarize_author())
    }
}

// **** Traits as Parameters ****
pub fn notify(item: &impl Summary) {
    println!("Breaking news! {}", item.summarize());
}

pub fn notify_2<T: Summary>(item: &T) {
    println!("Inside notify_2: {}", item.summarize());
}

pub fn notify_3<T: Summary, U: Summary>(item1: &T, item2: &U) {
    println!(
        "Inside notify_3: {0}\n{1}",
        item1.summarize(),
        item2.summarize()
    );
}

pub fn notify_4<T: Summary + Display>(item: &T) {
    println!(
        "Inside notify_4:\nitem:\n\t{item}\nitem.summarize():\n\t{0}",
        item.summarize()
    );
}

// Alternate syntax for specifying trait bounds ('where' clause)
pub fn notify_5_1<T: Summary + Display, U: SummaryDefaultImpl + Display>(t: &T, u: &U) {
    println!("some value\n")
}

pub fn notify_5_2<T, U>(t: &T, u: &U)
where
    T: Summary + Display,
    U: SummaryDefaultImpl + Display,
{
    println!("some value\n")
}


// **** Returning Types that Implement Traits ****
pub fn returns_summarizable() -> impl Summary {
    Tweet {
        username: String::from("horse_ebooks"),
        content: String::from(
            "of course, as you probably already know, people",
        ),
        reply: false,
        retweet: false,
    }
}


// **** Using Trait Bounds to Conditionally Implement Methods ****
pub struct Pair<T> {
    x: T,
    y: T,
}

impl<T> Pair<T> {
    pub fn new(x: T, y: T) -> Self {
        Self { x, y }
    }
}

impl<T: Display + PartialOrd> Pair<T> {
    pub fn cmp_display(&self) {
        if self.x >= self.y {
            println!("The largest member is x = {}\n", self.x);
        } else {
            println!("The largest member is y = {}\n", self.y);
        }
    }
}

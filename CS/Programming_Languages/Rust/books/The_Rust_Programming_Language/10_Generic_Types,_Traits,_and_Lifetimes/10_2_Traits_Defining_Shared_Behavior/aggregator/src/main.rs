use aggregator::*;

fn main() {
    // **** Implementing a Trait on a Type ****
    let tweet = Tweet {
        username: String::from("horse_ebooks"),
        content: String::from("of course, as you probably already know, people"),
        reply: false,
        retweet: false,
    };

    println!("1 new tweet: {}\n", Summary::summarize(&tweet));

    // Default Implementations
    let article = NewsArticle {
        headline: String::from("Penguins win the Stanley Cup Championship!"),
        location: String::from("Pittsburgh, PA, USA"),
        author: String::from("Iceburgh"),
        content: String::from(
            "The Pittsburgh Penguins once again are the best \
             hockey team in the NHL.",
        ),
    };

    println!(
        "New article available! {}\n",
        SummaryDefaultImpl::summarize(&article)
    );
    println!("1 new tweet: {}\n", SummaryDefaultImpl_2::summarize(&tweet));

    // Traits as Parameters
    println!("notify():");
    notify(&article);
    notify(&tweet);
    println!();
    
    println!("notify_2<T: Summary>():");
    notify_2(&article);
    notify_2(&tweet);
    println!();
    
    println!("notify_3<T: Summary, U: Summary>():");
    notify_3(&article, &tweet);
    
    println!("notify_4<T: Summary + Display>():");
    notify_4(&article);
    
    println!("notify_5<T, U>():\nwhere\n\tT: Summary + Display,\n\tU: SummaryDefaultImpl + Display");
    notify_5_2(&article, &tweet);
    
    // Returning Types that Implement Traits
    println!(
        "returns_summarizable():\n{}\n",
        returns_summarizable().summarize()
    );
    
    // Using Trait Bounds to Conditionally Implement Methods
    println!("Using Trait Bounds to Conditionally Implement Methods:");
    let p: Pair<i32> = Pair::new(5, 10);
    p.cmp_display();
}

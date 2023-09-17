//! 17.3. Implementing an Object-Oriented Design Pattern

pub struct Post {
    state: Option<Box<dyn State>>,
    content: String,
}

impl Post {
    pub fn new() -> Post {
        Post {
            state: Some(Box::new(Draft {})),
            content: String::new(),
        }
    }

    pub fn add_text(&mut self, text: &str) {
        self.content.push_str(text)
    }

    pub fn content(&self) -> &str {
        self.state.as_ref().unwrap().content(self)
    }

    pub fn request_review(&mut self) {
        if let Some(s) = self.state.take() {
            self.state = Some(s.request_review())
        }
    }

    pub fn approve(&mut self) {
        if let Some(s) = self.state.take() {
            self.state = Some(s.approve())
        }
    }
    
    pub fn reject(&mut self) {
        if let Some(s) = self.state.take() {
            self.state = Some(s.reject())
        }
    }
}

trait State {
    fn request_review(self: Box<Self>) -> Box<dyn State>;
    fn approve(self: Box<Self>) -> Box<dyn State>;
    fn content<'a>(&self, post: &'a Post) -> &'a str {
        ""
    }
    // Add a reject method that changes the post’s state from PendingReview back to Draft.
    fn reject(self: Box<Self>) -> Box<dyn State>;
}

struct Draft {}

impl State for Draft {
    fn request_review(self: Box<Self>) -> Box<dyn State> {
        Box::new(PendingReview {
            approvemnet_request_counter: 0,
        })
    }

    fn approve(self: Box<Self>) -> Box<dyn State> {
        self
    }
    
    fn reject(self: Box<Self>) -> Box<dyn State> {
        self
    }
}


struct PendingReview {
    // Require two calls to approve before the state can be changed to Published.
    approvemnet_request_counter: i8,
}

impl State for PendingReview {
    fn request_review(self: Box<Self>) -> Box<dyn State> {
        self
    }

    fn approve(self: Box<Self>) -> Box<dyn State> {
        match self.approvemnet_request_counter {
            0 => {
                Box::new(PendingReview {
                    approvemnet_request_counter: 1
                })
            },
            _ => {
                Box::new(Published {})
            }
        }
    }
    
    fn reject(self: Box<Self>) -> Box<dyn State> {
        Box::new(Draft {})
    }
}

struct Published {}

impl State for Published {
    fn request_review(self: Box<Self>) -> Box<dyn State> {
        self
    }

    fn approve(self: Box<Self>) -> Box<dyn State> {
        self
    }
    
    fn content<'a>(&self, post: &'a Post) -> &'a str {
        &post.content
    }
    
    fn reject(self: Box<Self>) -> Box<dyn State> {
        self
    }
}


#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn it_works() {}
}

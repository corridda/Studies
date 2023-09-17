#[derive(Debug)]
struct Rectangle {
    width: u32,
    hight: u32,
}

impl Rectangle {
    fn can_hold(&self, other: &Rectangle) -> bool {
        self.width > other.width && self.hight > other.hight
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn larger_can_hold_smaller() {
        let larger = Rectangle {
            width: 8,
            hight: 7
        };
        let smaller = Rectangle {
            width: 5,
            hight: 1                
        };
        assert!(larger.can_hold(&smaller))
    }

    #[test]
    fn smaller_cannot_hold_larger() {
        let larger = Rectangle {
            width: 8,
            hight: 7
        };
        let smaller = Rectangle {
            width: 5,
            hight: 1                
        };
        assert!(!smaller.can_hold(&larger))
    }

}

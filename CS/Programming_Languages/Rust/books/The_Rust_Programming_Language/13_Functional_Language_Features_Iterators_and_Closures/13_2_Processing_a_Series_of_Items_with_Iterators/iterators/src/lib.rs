#[derive(PartialEq, Debug)]
struct Shoe {
    size: i32,
    style: String,
}

fn shoes_in_size(shoes: Vec<Shoe>, shoe_size: i32) -> Vec<Shoe> {
    shoes.into_iter().filter(|s| s.size == shoe_size).collect()
}

#[cfg(test)]
mod tests {
    use super::*;
    
    #[test]
    fn iterator_demonstration() {
        /// The Iterator Trait and the 'next'-method
        let v1 = vec![1, 2, 3];

        let mut v1_iter = v1.iter();

        assert_eq!(v1_iter.next(), Some(&1));
        assert_eq!(v1_iter.next(), Some(&2));
        assert_eq!(v1_iter.next(), Some(&3));
        assert_eq!(v1_iter.next(), None);
    }

    #[test]
    fn iterator_sum() {
        /// Methods that Consume the Iterator
        let v = vec![1, 2, 3];
        let v_iter = v.iter();
        let v_sum: i32 = v_iter.sum();
        assert_eq!(v_sum, 6);
    }

    #[test]
    fn iterator_map() {
        /// Methods that Produce Other Iterators
        let v = vec![1, 2, 3];
        let v_mapped: Vec<_> = v.iter().map(|x| x + 1).collect();
        assert_eq!(v_mapped, vec![2, 3, 4]);
    }

    #[test]
    fn filters_by_size() {
        let shoes = vec![
            Shoe {
                size: 10,
                style: String::from("sneaker"),
            },
            Shoe {
                size: 13,
                style: String::from("sandal"),
            },
            Shoe {
                size: 10,
                style: String::from("boot"),
            },
        ];
        
        let my_size = 10;
        let in_my_size = shoes_in_size(shoes, my_size);

        assert_eq!(
            in_my_size,
            vec![
                Shoe {
                    size: 10,
                    style: String::from("sneaker")
                },
                Shoe {
                    size: 10,
                    style: String::from("boot")
                },
            ]
        );
        println!("in_my_size:\n{in_my_size:?}\nmy_size:\n{my_size}");
    }
}

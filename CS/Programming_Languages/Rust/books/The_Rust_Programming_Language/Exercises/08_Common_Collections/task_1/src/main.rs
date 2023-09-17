// Given a list of integers, use a vector and return the median
// (when sorted, the value in the middle position) and mode (the value that occurs most often;
// a hash map will be helpful here) of the list.

use std::collections::HashMap;
use rand::distributions::{Distribution, Uniform};

fn get_median(v: &mut Vec<u32>, middle_idx: usize) -> u32 {
    let sorted = v.select_nth_unstable(middle_idx);
    println!("{0:?} - {1} - {2:?}", sorted.0, sorted.1, sorted.2);
    *sorted.1
}

fn get_mode(v: &Vec<u32>) -> u32 {
    let mut count: HashMap<u32, usize> = HashMap::new();
    for key in v {
        *count.entry(*key).or_insert(0) += 1;
    }
//    println!("count: {count:?}\n");
    let mut count_vec: Vec<(&u32, &usize)> = count.iter().collect();
//    println!("count_vec: {count_vec:?}\n");
    count_vec.sort_by_key(|k| k.1);
    println!("sorted count_vec: {count_vec:?}");
    count_vec.reverse();
    *count_vec[0].0
}

fn main() {
    let mut v: Vec<u32> = Vec::new();
    let between = Uniform::from(0..=15);
    let mut rng = rand::thread_rng();
    for _ in 0..21 {
        v.push(between.sample(&mut rng))
    }
    
    let parity = v.len() % 2;
    let middle_idx: usize;
    if parity == 0 {
        middle_idx = v.len() / 2
    }
    else {
        middle_idx = v.len() / 2 + 1 
    }
    
    let median = get_median(&mut v, middle_idx);
    println!("median: {median}\n");
    
    let mode = get_mode(&v);
    println!("mode: {mode}\n");
}

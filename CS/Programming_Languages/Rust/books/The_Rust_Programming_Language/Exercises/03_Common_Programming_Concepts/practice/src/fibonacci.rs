pub mod fibo {
    pub fn get_nth_fibo(n: u32) -> u128 {
        let mut prev_fib_num: u128 = 0;
        let mut cur_fib_num: u128 = 1;
        if n == 1 {
            return prev_fib_num;
        } else if n == 2 {
            return cur_fib_num;
        } else {
            for _ in (3..n + 1) {
                let temp = prev_fib_num;
                prev_fib_num = cur_fib_num;
                cur_fib_num += temp;
            }
        }
        cur_fib_num
    }
}

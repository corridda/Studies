"""3. Find all positive divisors of the following integers:
(a) 20 (b) 52 (c) 195 (d) 203"""

from books.Mathematics.Number_Theory.Kraft_JS_Washington_LC. \
    Elementary_Number_Theory.chapter_1.exercises._1_2_divisibility. \
    auxiliary import get_all_positive_divisors


def main():
    n_list = [20, 52, 195, 203]
    for n in n_list:
        print(get_all_positive_divisors(n))


if __name__ == '__main__':
    main()

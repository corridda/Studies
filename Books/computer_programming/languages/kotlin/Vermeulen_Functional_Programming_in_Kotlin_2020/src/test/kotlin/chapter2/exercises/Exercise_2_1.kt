package chapter2.exercises

import io.kotlintest.shouldBe
import io.kotlintest.specs.WordSpec
import kotlinx.collections.immutable.persistentMapOf

class Exercise_2_1 : WordSpec({
    // tag::init[]
    fun fib(i: Int): Int {
        fun go(cur_num: Int): Int =
            if (cur_num < 1) 0
            else {
                when (cur_num) {
                    1, 2 -> 1
                    else -> go(cur_num - 1) + go(cur_num - 2)
                }
            }
        return go(i)
    }
    // end::init[]

    /**
     * Re-enable the tests by removing the `!` prefix!
     */
    "fib" should {
        "return the nth fibonacci number" {
            persistentMapOf(
                Pair(1, 1),
                Pair(2, 1),
                Pair(3, 2),
                Pair(4, 3),
                Pair(5, 5),
                Pair(6, 8),
                Pair(7, 13),
                Pair(8, 21)
            ).forEach { (n, num) ->
                fib(n) shouldBe num
            }
        }
    }
})

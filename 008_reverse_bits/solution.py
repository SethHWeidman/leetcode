# This was my first problem ever using bit manipulation! There are a few key "tricks" to know that
# can be combined to solve this problem: if `n` is a binary number
# 1. `n & 1` produces the rightmost digit of `n`
# 2. n <<= 1 shifts the binary characters of `n` to the left, multiplying the underlying number by
#    2, and adding a `0` to the right of the binary representation
# 3. n | [0|1] will set the rightmost character of `n` to be [0|1], if the rightmost character is
#    `0`
#
# In this problem, we'll combine 2 and 3 to shift the binary characters of `n` to the left and then
# `|` with the rightmost character that we've popped off another binary number
#
# 4. n >>= 1 shifts the binary characters of `n` to the right, dividing the underlying decimal
#    number by 2 and dropping the remainder


class Solution:
    def reverse_bits(self, n: int) -> int:
        new = 0
        for _ in range(32):  # guaranteed to be the length of `n`
            rightmost_bit = n & 1
            new <<= 1
            new |= rightmost_bit
            n >>= 1
        return new


if __name__ == '__main__':
    s = Solution()

    assert s.reverse_bits(int('00000010100101000001111010011100', 2)) == int(
        '00000010100101000001111010011100'[::-1], 2
    )
    assert s.reverse_bits(int('11111111111111111111111111111101', 2)) == int(
        '11111111111111111111111111111101'[::-1], 2
    )

    print("Simple test cases passed!")

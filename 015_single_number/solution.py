import typing


class Solution:
    def single_number(self, nums: typing.List[int]) -> int:
        # The naive solution here is:
        #
        #   d = {}
        #   for num in nums:
        #       if num not in d:
        #           d[num] = 1
        #       else:
        #           del d[num]
        #   return list(d.keys())[0]
        #
        # However, there is a "trick" solution given by bit manipulation:
        #
        # The XOR operation is:
        #   * Associative (a ^ (b ^ c) = (a ^ b) ^ c). The cases where a, b, and c are all 0 are
        #     trivial. Taking the other six cases
        #     * (0 ^ (0 ^ 1) = (0 ^ 0) ^ 1 = 1
        #     * (0 ^ (1 ^ 0) = (0 ^ 1) ^ 0 = 1
        #     * (1 ^ (0 ^ 0) = (1 ^ 0) ^ 0 = 1
        #     * (1 ^ (1 ^ 0) = (1 ^ 1) ^ 0 = 0
        #     * (1 ^ (0 ^ 1) = (1 ^ 0) ^ 1 = 0
        #     * (0 ^ (1 ^ 1) = (0 ^ 1) ^ 1 = 0
        #     * (1 ^ (1 ^ 1) = (1 ^ 1) ^ 1 = 1
        #   (Notice even here: the cases with an odd number of `1`s evaluate to 1, and those with
        #   an even number of `1`s evaluate to `0`)
        #   * Commutative: (a ^ b) = (b ^ a)
        #
        # Finally, combining those insights with another couple basic facts:
        #   * (a ^ 0) = a
        #   * (a ^ a) = 0
        # We see that simply "XORing" all the numbers in `nums` together will produce the one
        # distinct number
        res = 0
        for num in nums:
            res ^= num
        return res


if __name__ == "__main__":
    s = Solution()

    assert s.single_number([2, 2, 1]) == 1
    assert s.single_number([4, 1, 2, 1, 2]) == 4
    assert s.single_number([1]) == 1

    print("Simple test cases passed!")

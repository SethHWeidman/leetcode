class Solution:
    def range_bitwise_and(self, left: int, right: int) -> int:
        # idea: shift left and right to the right - once we find they are equal, this means we have
        # found a common "prefix", so shift back to the left that many steps, since everything else
        # will have been "OR"ed away by the elements not in common
        shift = 0
        while left != right:
            left >>= 1
            right >>= 1
            shift += 1

        return left << shift


if __name__ == "__main__":
    s = Solution()

    assert s.range_bitwise_and(5, 7) == 4
    assert s.range_bitwise_and(0, 0) == 0
    assert s.range_bitwise_and(0, 2147483647) == 0

    print("All test cases passed!")

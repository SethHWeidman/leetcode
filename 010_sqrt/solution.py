class Solution:
    def my_sqrt(self, x: int) -> int:
        if x < 2:  # 0 and 1 are their own roots
            return x
        left = 0
        right = x // 2  # √x < x / 2 for x ≥ 4
        ans = 1

        # binary search between 0 and x // 2
        while left <= right:
            mid = (left + right) // 2
            sq = mid * mid  # `*` is noticably cheaper than `**`
            if sq <= x:
                ans = mid  # mid is still a valid floor-sqrt
                left = mid + 1  # try something larger
            else:
                right = mid - 1  # mid² too big - shrink the range
        return ans


if __name__ == "__main__":

    s = Solution()

    assert s.my_sqrt(4) == 2
    assert s.my_sqrt(8) == 2

    print("Simple test cases passed!")

class Solution:
    def my_sqrt(self, x: int) -> int:
        if x < 2:
            return x
        left = 0
        right = x // 2

        # binary search between 0 and x // 2
        while left < right:
            mid = left + (right - left) // 2
            sq = mid**2
            sq_plus_one = (mid + 1) ** 2
            if sq == x:
                return mid
            elif sq > x:
                right = mid
            elif sq < x:
                if sq_plus_one > x:
                    return mid
                left = mid + 1
        return left


if __name__ == "__main__":

    s = Solution()

    assert s.my_sqrt(4) == 2
    assert s.my_sqrt(8) == 2

    print("Simple test cases passed!")

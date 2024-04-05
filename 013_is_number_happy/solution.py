class Solution:
    def is_happy(self, n: int) -> bool:
        nums = {n}
        # note that it is impossible for this to loop forever
        while True:
            n = self.sum_of_squares(n)
            if n == 1:
                return True
            if n in nums:
                return False
            nums.add(n)

    def sum_of_squares(self, n: int) -> bool:
        total = 0
        while n > 0:
            n, ones = divmod(n, 10)
            total += ones**2
        return total


if __name__ == "__main__":

    s = Solution()

    assert s.is_happy(19)
    assert not s.is_happy(2)

    print("Simple test cases passed!")

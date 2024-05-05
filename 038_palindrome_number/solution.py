class Solution:
    def is_palindrome(self, x: int) -> bool:
        if x < 0 or (x > 0 and x % 10 == 0):
            return False
        elif x == 0:
            return True

        new = 0
        while x > new:
            x_w_o_last_digit = x // 10
            last_digit = x - (x_w_o_last_digit * 10)
            new = new * 10 + last_digit
            x = x_w_o_last_digit

        return new == x or x == new // 10


if __name__ == "__main__":
    s = Solution()

    assert s.is_palindrome(0)
    assert s.is_palindrome(121)
    assert not s.is_palindrome(-121)
    assert not s.is_palindrome(10)

    print("Simple test cases passed!")

class Solution:
    def is_palindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1

        while left < right:

            while left < right and not s[left].isalnum():
                left += 1

            while left < right and not s[right].isalnum():
                right -= 1

            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True


if __name__ == "__main__":
    s = Solution()

    assert s.is_palindrome("A man, a plan, a canal: Panama")
    assert not s.is_palindrome("race a car")
    assert s.is_palindrome(" ")

    print("Simple test cases passed!")

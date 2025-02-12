class Solution:
    def longest_palindrome(self, s: str) -> str:

        longest = 0

        def _longest_palindrome_centered_left_right(left: int, right: int) -> int:

            while left >= 0 and right <= len(s) - 1 and s[left] == s[right]:
                left -= 1
                right += 1

            return right - left - 1 if right > left else 0

        for i in range(len(s)):

            l1 = _longest_palindrome_centered_left_right(i, i)
            l2 = _longest_palindrome_centered_left_right(i, i + 1)

            max_len = max(l1, l2)

            if max_len > longest:
                longest = max_len

                start = i - (max_len - 1) // 2
                end = i + max_len // 2

        return s[start : end + 1]


if __name__ == "__main__":
    s = Solution()

    assert s.longest_palindrome("babad") == "bab"
    assert s.longest_palindrome("cbbd") == "bb"

    print("Simple test cases passed!")

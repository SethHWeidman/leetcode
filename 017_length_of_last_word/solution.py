class Solution:
    def length_of_last_word(self, s: str) -> int:
        n = len(s)
        cnt = 0
        for i in range(n - 1, -1, -1):
            # first need to iterate through any initial spaces
            if s[i].isspace():
                continue
            if s[i].isalpha():
                cnt += 1
            if s[i - 1].isspace():
                break
        return cnt


if __name__ == "__main__":
    s = Solution()

    assert s.length_of_last_word("Hello World") == 5
    assert s.length_of_last_word("   fly me   to   the moon  ") == 4
    assert s.length_of_last_word("luffy is still joyboy") == 6

    print("Simple test cases passed!")

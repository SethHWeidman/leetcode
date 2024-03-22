class Solution(object):
    def is_subsequence(self, s: str, t: str) -> bool:
        # The idea here is:
        # Suppose the characters of `s` are "a", b, c, etc.
        # First, search t for "a". Once you find "a", start searching for "b" where you found "a",
        # etc.
        # If you reach the end of `s`, you are done
        # Otherwise, if you reach the end of `t` without seeing all the characters in `s`, return
        # False
        # Finally, just as the empty set is a member of every set, return True if `len(s)` is 0
        # The code below does exactly this:
        if not len(s):
            return True
        index_s, index_t = 0, 0
        s_char = s[index_s]
        while index_t < len(t):
            if t[index_t] == s_char:
                index_s += 1
                if index_s == len(s):
                    return True
                s_char = s[index_s]
            index_t += 1
        return False


if __name__ == "__main__":
    s = Solution()

    assert s.is_subsequence("abc", "ahbgdc")
    assert not s.is_subsequence("axc", "ahbgdc")
    assert s.is_subsequence("", "ahbgdc")

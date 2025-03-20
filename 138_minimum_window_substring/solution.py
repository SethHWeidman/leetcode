import collections


class Solution:
    def minimum_window_substring(self, s: str, t: str) -> str:
        # idea:
        # keep a counter of distinct characters in `t`
        counter_t = collections.Counter(t)

        counter_s = collections.defaultdict(int)

        # number of distinct characters in `t` that have the correct number of characters "formed"
        formed = 0

        # number of total distinct characters in `t`
        n = len(counter_t)

        # pointers to the left and right characters of the string
        l, r = 0, 0

        # store the length, and left and right characters of the minimal substring
        ans = float("inf"), 0, 0

        while r < len(s):
            char = s[r]
            counter_s[char] += 1

            if char in counter_t and counter_t[char] == counter_s[char]:
                formed += 1

            # contract the window until one of the characters in the window no longer has as
            # occurences as it does in `t`
            while formed == n and l <= r:

                if r - l + 1 < ans[0]:
                    ans = r - l + 1, l, r

                char_l = s[l]
                counter_s[char_l] -= 1

                if char_l in counter_t and counter_s[char_l] < counter_t[char_l]:
                    formed -= 1

                l += 1

            r += 1

        return "" if ans[0] == float("inf") else s[ans[1] : ans[2] + 1]


if __name__ == "__main__":
    s = Solution()

    assert s.minimum_window_substring("ADOBECODEBANC", "ABC") == "BANC"
    assert s.minimum_window_substring("a", "a") == "a"
    assert s.minimum_window_substring("a", "aa") == ""

    print("Simple test cases passed!")

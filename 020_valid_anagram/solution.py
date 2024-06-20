import collections


class Solution:
    def is_anagram(self, s: str, t: str) -> bool:
        s_dict = collections.defaultdict(int)
        t_dict = collections.defaultdict(int)
        chars = set()

        for char in s:
            s_dict[char] += 1
            chars.add(char)

        for char in t:
            t_dict[char] += 1
            chars.add(char)

        for char in chars:
            if s_dict[char] != t_dict[char]:
                return False

        return True


if __name__ == '__main__':
    s = Solution()

    assert s.is_anagram("anagram", "nagaram")
    assert not s.is_anagram("rat", "car")
    assert not s.is_anagram("a", "ab")

    print("Simple test cases passed!")

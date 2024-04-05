class Solution:
    def can_construct(self, ransom_note: str, magazine: str) -> bool:
        magazine_counter = {}
        for char in magazine:
            if char not in magazine_counter:
                magazine_counter[char] = 1
            else:
                magazine_counter[char] += 1

        for char in ransom_note:
            if char not in magazine_counter:
                return False
            else:
                magazine_counter[char] -= 1
                if magazine_counter[char] < 0:
                    return False
        return True


if __name__ == "__main__":

    s = Solution()

    assert not s.can_construct("a", "b")
    assert not s.can_construct("aa", "ab")
    assert s.can_construct("aa", "aab")

    print("Simple test cases passed!")

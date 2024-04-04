class Solution:
    def word_pattern(self, pattern: str, s: str) -> bool:
        # simple "two hashmaps" solution
        words = s.split(' ')
        n = len(pattern)
        if n != len(words):
            return False

        word_to_char = {}
        char_to_word = {}

        for i in range(n):
            word = words[i]
            char = pattern[i]

            if word in word_to_char and word_to_char[word] != char:
                return False
            if char in char_to_word and char_to_word[char] != word:
                return False

            word_to_char[word] = char
            char_to_word[char] = word
        return True


if __name__ == "__main__":

    s = Solution()

    assert s.word_pattern("abba", "dog cat cat dog")
    assert not s.word_pattern("abba", "dog cat cat fish")
    assert not s.word_pattern("aaaa", "dog cat cat dog")

    print("Simple test cases passed!")

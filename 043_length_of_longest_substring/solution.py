class Solution:
    def length_of_longest_substring(self, s: str) -> int:
        # Length of the longest substring without repeating characters
        max_len = 0

        # If we keep track of, at each point in the string, the starting point of the preceding
        # substring that has no repeating characters, then one additional line will be able to
        # compute the longest substring we've seen so far
        start = 0
        # `char_index_map` turns out to be key to help us properly keep track of `start`; it tracks
        # the maximum index of each character in the string so far
        char_index_map = {}

        for i, char in enumerate(s):
            # Does seening `char` at this index newly create a substring with duplicates? If so,
            # update `start` appropriately
            if char in char_index_map and char_index_map[char] >= start:
                # If the last time we saw `char` was at `i`, we now only need to consider
                # substrings starting at `i + 1`
                start = char_index_map[char] + 1
            # Clearly the new maximum index at which we've seen `char` is `i`
            char_index_map[char] = i

            # Assuming we've kept track of `start` properly, this should update the maximum length
            # of the substring we've seen
            max_len = max(max_len, i - start + 1)
        return max_len


if __name__ == "__main__":
    solution = Solution()

    assert solution.length_of_longest_substring("abcabcbb") == 3
    assert solution.length_of_longest_substring("bbbbb") == 1
    assert solution.length_of_longest_substring("pwwkew") == 3
    assert solution.length_of_longest_substring("abba") == 2
    assert solution.length_of_longest_substring("dvdf") == 3

    print("Simple test cases passed!")

import collections


def lists_of_lists_to_set(list1: list[list]) -> set:
    return set(frozenset(inner_list) for inner_list in list1)


class Solution:
    def group_anagrams(self, strs: list[str]) -> list[list[str]]:
        str_char_tuple_to_str_dict = collections.defaultdict(list)

        for s in strs:
            str_char_list = [0] * 26
            for char in s:
                char_ord = ord(char) - ord('a')
                str_char_list[char_ord] += 1
            str_char_tuple_to_str_dict[tuple(str_char_list)].append(s)

        return list(str_char_tuple_to_str_dict.values())


if __name__ == "__main__":
    s = Solution()

    assert lists_of_lists_to_set(
        s.group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    ) == lists_of_lists_to_set([["bat"], ["nat", "tan"], ["ate", "eat", "tea"]])
    assert s.group_anagrams([""]) == [[""]]
    assert s.group_anagrams(["a"]) == [["a"]]

    print("Simple test cases passed!")

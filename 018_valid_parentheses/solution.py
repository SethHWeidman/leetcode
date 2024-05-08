class Solution:
    def is_valid(self, s: str) -> bool:
        stack = []

        lookup = {')': '(', ']': '[', '}': '{'}

        for char in s:
            if char not in lookup:  # `char` is a "start paren"
                stack.append(char)
            else:  # `char` is a "start paren"
                if len(stack) == 0:
                    return False
                last_paren = stack.pop()
                if last_paren != lookup[char]:
                    return False
        return len(stack) == 0


if __name__ == "__main__":
    s = Solution()

    assert not s.is_valid("[")
    assert s.is_valid("()")
    assert s.is_valid("()[]{}")
    assert not s.is_valid("(]")
    assert not s.is_valid("([)]")

    print("Simple test cases passed!")

class Solution:
    def roman_to_int(self, s: str) -> int:
        total = 0
        index = 0
        str_len = len(s)

        char_values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1_000}

        # the algorithm for Roman numeral computation can be described as follows: proceed
        # character by character. Normally, add the value of each character to a running total - we
        # can call this "case 1". However, if we get to a pair of characters for which the second
        # character has a larger value than the first character, add the difference between their
        # values to the running total - we can call this "case 2".
        while index < str_len:
            current_char = s[index]
            value_current_char = char_values[current_char]
            if index < str_len - 1:
                next_char = s[index + 1]
                value_next_char = char_values[next_char]
                # "case 2"
                if value_current_char < value_next_char:
                    total += value_next_char - value_current_char
                    index += 2
                # "case 1"
                else:
                    total += value_current_char
                    index += 1
            # "case 1"
            else:
                total += value_current_char
                index += 1
        return total


if __name__ == "__main__":
    solution = Solution()

    assert solution.roman_to_int("III") == 3
    assert solution.roman_to_int("LVIII") == 58
    assert solution.roman_to_int("MCMXCIV") == 1994

    print("Simple test cases passed!")
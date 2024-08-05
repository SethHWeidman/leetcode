import typing


class Solution:
    def full_justify(self, words: typing.List[str], max_width: int) -> typing.List[str]:
        lines = []

        current_line_words_length = 0
        current_line_words = []
        for word in words:

            # either: we need to create a `line` and start a new one...
            if current_line_words_length + len(word) > max_width:

                if len(current_line_words) > 1:
                    num_spaces, extra_spaces = divmod(
                        (max_width - (current_line_words_length - len(current_line_words))),
                        len(current_line_words) - 1,
                    )

                    for i in range(extra_spaces):
                        current_line_words[i] = current_line_words[i] + ' '

                    current_line = (" " * num_spaces).join(current_line_words)
                else:
                    the_only_word = current_line_words[0]
                    current_line = the_only_word + " " * (max_width - len(the_only_word))

                lines.append(current_line)

                current_line_words_length = len(word) + 1
                current_line_words = [word]

            # ...or: we need not
            else:
                current_line_words_length += len(word) + 1
                current_line_words.append(word)

        last_line = " ".join(current_line_words)
        last_line += " " * (max_width - len(last_line))
        lines.append(last_line)
        return lines


if __name__ == "__main__":
    s = Solution()

    assert s.full_justify(["This", "is", "an", "example", "of", "text", "justification."], 16) == [
        "This    is    an",
        "example  of text",
        "justification.  ",
    ]

    assert s.full_justify(["What", "must", "be", "acknowledgment", "shall", "be"], 16) == [
        "What   must   be",
        "acknowledgment  ",
        "shall be        ",
    ]

    assert s.full_justify(
        [
            "Science",
            "is",
            "what",
            "we",
            "understand",
            "well",
            "enough",
            "to",
            "explain",
            "to",
            "a",
            "computer.",
            "Art",
            "is",
            "everything",
            "else",
            "we",
            "do",
        ],
        20,
    ) == [
        "Science  is  what we",
        "understand      well",
        "enough to explain to",
        "a  computer.  Art is",
        "everything  else  we",
        "do                  ",
    ]

    print("All test cases passed!")

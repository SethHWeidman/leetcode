class Solution:
    def summary_ranges(self, nums: list[int]) -> list[str]:
        if not len(nums):
            return []

        answers = []

        start = nums[0]
        for i in range(1, len(nums)):
            # we need to add an answer
            if nums[i - 1] + 1 != nums[i]:
                if nums[i - 1] != start:
                    answers.append(f"{start}->{nums[i-1]}")
                else:
                    answers.append(f"{start}")
                start = nums[i]

        # handle the end
        if nums[-1] != start:
            answers.append(f"{start}->{nums[-1]}")
        else:
            answers.append(f"{nums[-1]}")

        return answers


if __name__ == "__main__":
    s = Solution()

    assert s.summary_ranges([]) == []
    assert s.summary_ranges([0, 1, 2, 4, 5, 7]) == ["0->2", "4->5", "7"]
    assert s.summary_ranges([0, 2, 3, 4, 6, 8, 9]) == ["0", "2->4", "6", "8->9"]

    print("Test cases passed!")
